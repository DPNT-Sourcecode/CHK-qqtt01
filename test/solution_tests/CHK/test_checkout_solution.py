from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_invalid_input(self):
        assert CheckoutSolution().checkout("") == 0
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout(None) == -1

    def test_checkout_each(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

    def test_multiple_product(self):
        assert CheckoutSolution().checkout("AA") == 100
        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15

    def test_discounts(self):
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAAAA") == 130 + 130
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("BBBB") == 45 * 2

    def test_product_have_no_discount(self):
        assert CheckoutSolution().checkout("CC") == 40
        assert CheckoutSolution().checkout("DD") == 30


