from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_invalid_input(self):
        assert CheckoutSolution().checkout("") == -1
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout([]) == -1

    def test_checkout_each(self):
        assert CheckoutSolution().checkout(["A"]) == 50
        assert CheckoutSolution().checkout(["B"]) == 30
        assert CheckoutSolution().checkout(["C"]) == 20
        assert CheckoutSolution().checkout(["D"]) == 15

