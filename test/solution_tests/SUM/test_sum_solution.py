from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_non_a_number(self):
        try:
            SumSolution().compute(1, "a")
        except TypeError:
            assert True

