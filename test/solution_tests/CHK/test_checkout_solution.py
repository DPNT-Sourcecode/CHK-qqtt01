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

    def test_multiple_product(self):
        assert CheckoutSolution().checkout(["A"] * 2) == 100
        assert CheckoutSolution().checkout(["A", "B", "C", "D"]) == 50 + 30 + 20 + 15

    def test_discounts(self):
        assert CheckoutSolution().checkout(["A", "A", "A"]) == 130
    #     assert CheckoutSolution().checkout(["B", "B"]) == 45
    #     assert CheckoutSolution().checkout(["A", "A", "B", "B"]) == 100 + 45
    #
    # def test_product_have_no_discount(self):
    #     assert CheckoutSolution().checkout(["C", "C"]) == 40
    #     assert CheckoutSolution().checkout(["D", "D"]) == 30



