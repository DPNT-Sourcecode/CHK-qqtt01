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
        assert CheckoutSolution().checkout("E") == 40
        assert CheckoutSolution().checkout("F") == 10

    def test_multiple_product(self):
        assert CheckoutSolution().checkout("AA") == 100
        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15

    def test_discounts(self):
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("A" * 6) == 200 + 50
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("BBBB") == 45 * 2

    def test_product_have_no_discount(self):
        assert CheckoutSolution().checkout("CC") == 40
        assert CheckoutSolution().checkout("DD") == 30

    def test_2es_gives_1b_free(self):
        assert CheckoutSolution().checkout("EEB") == 40 + 40
        assert CheckoutSolution().checkout("EEEEBB") == 40 * 4

    def test_2e_no_b_to_discount(self):
        # 2E without B still charges 2E only
        assert CheckoutSolution().checkout("EE") == 80

    def test_e_and_multiple_b_discount_limited(self):
        # 2E can remove only one B
        assert CheckoutSolution().checkout("EEBBB") == 125  # one B is free

    def test_odd_number_of_es_and_bs(self):
        # 5E gives 2B free, 1E no additional effect
        assert CheckoutSolution().checkout("EEEEE" + "BBB") == 40 * 5 + 30 * 1

    def test_discount_priority_on_a(self):
        # 5A should apply 5A for 200, not 3A+2A
        assert CheckoutSolution().checkout("A" * 5) == 200

    def test_mixed_items_with_all_discounts(self):
        # 5A (200), 2B (45), 2E (1B free), 1B charged
        assert CheckoutSolution().checkout("AAAAABBEE") == 200 + 80 + 30

    def test_f_offer_exactly_three(self):
        assert CheckoutSolution().checkout("F" * 2) == 20

    def test_f_offer_with_remainder(self):
        assert CheckoutSolution().checkout("F" * 4) == 20 + 10

    def test_f_offer_multiple_sets(self):
        assert CheckoutSolution().checkout("F" * 5) == 20 + 10 + 10

    def test_from_output(self):
        assert CheckoutSolution().checkout("a") == -1
        assert CheckoutSolution().checkout("-") == -1
        assert CheckoutSolution().checkout("ABCa") == -1
        assert CheckoutSolution().checkout("AxA") == -1
        assert CheckoutSolution().checkout("ABCDE") == 155
        assert CheckoutSolution().checkout("AA") == 100
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("AAAAAAA") == 300
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
        assert CheckoutSolution().checkout("AAAAAAAAA") == 380
        assert CheckoutSolution().checkout("AAAAAAAAAA") == 400
        assert CheckoutSolution().checkout("EE") == 80
        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEEB") == 120
        assert CheckoutSolution().checkout("EEEEBB") == 160
        assert CheckoutSolution().checkout("BEBEEE") == 160
        assert CheckoutSolution().checkout("BBB") == 75
        assert CheckoutSolution().checkout("BBBB") == 90
        assert CheckoutSolution().checkout("ABCDEABCDE") == 280
        assert CheckoutSolution().checkout("CCADDEEBBA") == 280
        assert CheckoutSolution().checkout("AAAAAEEBAAABB") == 455
        assert CheckoutSolution().checkout("ABCDECBAABCABBAAAEEAA") == 665



