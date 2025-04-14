from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_invalid_input(self):
        assert CheckoutSolution().checkout("") == -1
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout([]) == -1
