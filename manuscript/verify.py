import hashlib
import json
from fractions import Fraction
from math import comb


OEIS_ROWS = {
    -3: [[1, -4, 1], [1, 3, 3, 1], [1, -14, -30, -14, 1],
         [1, 17, 262, 262, 17, 1],
         [1, 79, 8157, 50003, 50003, 8157, 79, 1]],
    -4: [[1, -6, 1], [1, 11, 11, 1], [1, -44, -154, -44, 1],
         [1, 117, 1562, 1562, 117, 1],
         [1, 1087, 95853, 568339, 568339, 95853, 1087, 1]],
    -5: [[1, -8, 1], [1, 23, 23, 1], [1, -106, -414, -106, 1],
         [1, 405, 5210, 5210, 405, 1],
         [1, 6547, 530721, 3079435, 3079435, 530721, 6547, 1]],
}
ODD_ALTERNATING = {
    -3: {3: 6, 5: 0, 7: 1296, 9: -155520, 11: 35271936},
    -4: {3: 8, 5: -64, 7: 9728, 9: -2289664},
    -5: {3: 10, 5: -200, 7: 40000, 9: -15200000},
}


def rows(step, maximum):
    previous = [1]
    yield 1, previous
    for row_number in range(2, maximum + 1):
        current = [1] * row_number
        for position in range(2, row_number):
            current[position - 1] = (
                (step * (row_number - position) + 1) * previous[position - 2]
                + (step * (position - 1) + 1) * previous[position - 1]
            )
        yield row_number, current
        previous = current


def check():
    results = []
    odd_congruence_rows = 0
    column_formula_rows = 0
    for step in list(range(-12, -2)) + [0, 1, 2, 3]:
        digest = hashlib.sha256()
        row_sum = 1
        second_previous = None
        entry_count = 0
        for row_number, current in rows(step, 400):
            entry_count += row_number
            assert current == current[::-1]
            if row_number >= 2:
                row_sum *= step * (row_number - 2) + 2
            assert sum(current) == row_sum
            alternating = sum(current[::2]) - sum(current[1::2])
            if row_number >= 2 and step != 0:
                expected_second = (Fraction(2 * (step + 1) ** (row_number - 1), step)
                                   - row_number + 1 - Fraction(2, step))
                assert current[1] == expected_second
                column_formula_rows += 1
            if step == -3 and row_number >= 3:
                expected_third = (Fraction((-5) ** row_number, 45)
                                  + (Fraction(5, 9) - Fraction(row_number, 3)) * (-2) ** row_number
                                  + Fraction(row_number ** 2, 2)
                                  - Fraction(13 * row_number, 6) + Fraction(20, 9))
                assert current[2] == expected_third
            if row_number % 2 == 1:
                if step % 3 == 1:
                    assert alternating % 3 == 1
                    expected_mod3 = [((-1) ** index * comb(row_number - 1, index)) % 3
                                     for index in range(row_number)]
                    assert [value % 3 for value in current] == expected_mod3
                    odd_congruence_rows += 1
                if step <= -4 and step % 4 == 0:
                    divisor = (-2 * step) ** ((row_number - 1) // 2)
                    quotient, remainder = divmod(alternating, divisor)
                    assert remainder == 0 and quotient % 2 == 1
                    odd_congruence_rows += 1
            if row_number % 2 == 0:
                assert min(current) > 0
                assert alternating == 0
                if step <= -3:
                    radius_parameter = -step
                    if second_previous is not None:
                        previous_number = row_number - 2
                        assert current[1] == (
                            (radius_parameter - 1) ** 2 * second_previous
                            + radius_parameter * (radius_parameter - 2) * previous_number
                            + 2 - radius_parameter ** 2
                        )
                    second_previous = current[1]
                ratios = [Fraction(current[index], current[index + 1])
                          for index in range(row_number - 1)]
                assert min(ratios) * max(ratios) == 1
            elif row_number >= 3 and step <= -3:
                assert max(current[1:-1]) < 0
            elif step >= 0:
                assert min(current) > 0
            if step in OEIS_ROWS and row_number in [3, 4, 5, 6, 8]:
                assert current == OEIS_ROWS[step][[3, 4, 5, 6, 8].index(row_number)]
            if step in ODD_ALTERNATING and row_number in ODD_ALTERNATING[step]:
                assert alternating == ODD_ALTERNATING[step][row_number]
            digest.update((str(row_number) + ':' + ','.join(map(str, current)) + '\n').encode())
        results.append({'m': step, 'rows': 400, 'entries': entry_count,
                        'row_stream_sha256': digest.hexdigest()})
    excluded = {}
    for step in [-2, -1]:
        current = list(rows(step, 4))[-1][1]
        assert current == [1, -1, -1, 1]
        excluded[str(step)] = current
    degenerate_rows = 0
    for step in [-2, -1]:
        for row_number, current in rows(step, 400):
            if row_number == 1:
                continue
            if row_number % 2 == 0:
                degree = row_number - 2
                expected = [binomial_coefficient(degree, index)
                            + binomial_coefficient(degree, index - 1)
                            for index in range(row_number)]
            elif step == -2:
                expected = [binomial_coefficient(row_number - 1, index)
                            for index in range(row_number)]
            else:
                degree = row_number - 3
                expected = [binomial_coefficient(degree, index)
                            + binomial_coefficient(degree, index - 2)
                            for index in range(row_number)]
            assert current == expected
            degenerate_rows += 1
    small_parameters = [Fraction(-13, 4), Fraction(-7, 2), Fraction(-9, 2),
                        Fraction(1, 4), Fraction(1, 2), Fraction(3, 2)]
    rational_entries = 0
    for step in small_parameters:
        for row_number, current in rows(step, 60):
            assert current == current[::-1]
            if step <= -3 and row_number % 2 == 0:
                assert min(current) > 0
            if step <= -3 and row_number >= 3 and row_number % 2 == 1:
                assert max(current[1:-1]) < 0
            if step > 0:
                assert min(current) > 0
            rational_entries += row_number
    column3_at100 = list(rows(-3, 100))[-1][1][2]
    assert column3_at100 > comb(99, 2) * 4 ** 100
    egf_comparisons = 0
    for radius_parameter in [3, 4, 5, 8, 12]:
        derivatives = [1]
        for order in range(120):
            derivative = 2 * sum(comb(order, index) * radius_parameter ** index
                                 * derivatives[order - index]
                                 for index in range(1, order + 1, 2))
            derivative -= sum(comb(order, index) * radius_parameter ** index
                              * derivatives[order - index + 1]
                              for index in range(2, order + 1, 2))
            derivatives.append(derivative)
        for row_number, current in rows(-radius_parameter, 121):
            assert sum(current[::2]) - sum(current[1::2]) == derivatives[row_number - 1]
            egf_comparisons += 1
    return {'schema_version': 1, 'status': 'all assertions satisfied',
            'arithmetic': 'exact integers and rational coefficient ratios',
            'coverage': ['symmetry', 'row-sum product', 'strict even-row positivity',
                         'even-row parity sums', 'odd-row interior negativity for m <= -3',
                         'second-column two-row identity', 'reciprocal coefficient ratios',
                         'selected OEIS initial rows and odd alternating sums',
                         'odd-row alternating-sum divisibility and congruences',
                         'characteristic-three polynomial identity',
                         'exact second- and third-column formulas',
                         'degenerate-step polynomial factorizations'],
            'parameters': results, 'excluded_integer_parameters': excluded,
            'odd_congruence_rows': odd_congruence_rows,
            'second_column_formula_rows': column_formula_rows,
            'degenerate_factorization_rows': degenerate_rows,
            'cosh_differential_identity_comparisons': egf_comparisons,
            'cosh_differential_identity': 'cosh(r*t) * F_prime(t) = 2*sinh(r*t) * F(t)',
            'root_contours': check_root_contours(),
            'rational_parameters': [str(step) for step in small_parameters],
            'rational_rows_per_parameter': 60, 'rational_entries': rational_entries,
            'root_bound_example': {'m': -3, 'n': 100, 'column3': str(column3_at100),
                                   'inequality': 'T(100,3) > binomial(99,2) * 4^100',
                                   'consequence': 'M_100(-3) > 2^100 by Vieta'},
            'scope': 'Finite checks through row 400; all-row statements have written proofs in note.pdf.'}


def binomial_coefficient(degree, index):
    if index < 0 or index > degree:
        return 0
    return (-1) ** index * comb(degree, index)


def check_root_contours():
    row_number = 400
    scale = 5 ** (row_number // 2)
    first = Fraction(2 ** row_number, 3) - row_number + Fraction(5, 3)
    second = (Fraction(5 ** row_number, 45)
              + (Fraction(5, 9) - Fraction(row_number, 3)) * 2 ** row_number
              + Fraction(row_number ** 2, 2)
              - Fraction(13 * row_number, 6) + Fraction(20, 9))
    epsilon = Fraction(4 * row_number ** 2 * 2 ** row_number, scale)
    comparisons = []
    for radius in [Fraction(1, 7), Fraction(1, 6)]:
        ratio = epsilon / radius
        assert ratio < 1
        tail = radius ** 2 * ratio ** 3 / (1 - ratio)
        perturbation = abs(first / scale) * radius
        perturbation += abs(second / scale ** 2 - Fraction(1, 45)) + tail
        margin = abs(radius ** 2 - Fraction(1, 45))
        assert perturbation < Fraction(1, 10 ** 6) < margin
        comparisons.append({'radius': str(radius), 'limiting_quadratic_margin': str(margin),
                            'perturbation_less_than': '1/1000000'})
    return {'m': -3, 'n': row_number, 'scale': '5^200',
            'contours': comparisons, 'roots_between_radii': 2,
            'all_roots_inside_outer_radius': True,
            'largest_root_interval': '5^200/7 < M_400(-3) < 5^200/6',
            'basis': 'Rouche inequality, exact column formulas and the proved uniform path bound'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2, sort_keys=True))
