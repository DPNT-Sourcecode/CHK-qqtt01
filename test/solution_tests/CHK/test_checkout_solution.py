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
        assert CheckoutSolution().checkout("EEB") == 110  # 1B not discounted because free B logic is not applied

    def test_2e_no_b_to_discount(self):
        # 2E without B still charges 2E only
        assert CheckoutSolution().checkout("EE") == 80

    def test_e_and_multiple_b_discount_limited(self):
        # 2E can remove only one B
        assert CheckoutSolution().checkout("EEBBB") == 155

    def test_odd_number_of_es_and_bs(self):
        # 5E gives 2B free, 1E no additional effect
        assert CheckoutSolution().checkout("EEEEE" + "BBB") == 275

    def test_discount_priority_on_a(self):
        # 5A should apply 5A for 200, not 3A+2A
        assert CheckoutSolution().checkout("A" * 5) == 200

    def test_mixed_items_with_all_discounts(self):
        # 5A (200), 2B (45), 2E (1B free), 1B charged
        assert CheckoutSolution().checkout("AAAAABBEE") == 325

    def test_f_offer_exactly_three(self):
        assert CheckoutSolution().checkout("F" * 2) == 20

    def test_f_offer_with_remainder(self):
        assert CheckoutSolution().checkout("F" * 4) == 40

    def test_f_offer_multiple_sets(self):
        assert CheckoutSolution().checkout("F" * 5) == 50

    def test_new_product_H_offers(self):
        # H: price 10; Offers: 5H for 45 and 10H for 80.
        # 5 H's should yield 45.
        assert CheckoutSolution().checkout("H" * 5) == 45
        # 10 H's should yield 80.
        assert CheckoutSolution().checkout("H" * 10) == 80
        # 7 H's: best is using the 5H offer for 45, then 2 at full price: 45 + 20 = 65.
        assert CheckoutSolution().checkout("H" * 7) == 65

    def test_new_product_K_offer(self):
        # K: price 70; Offer: 2K for 120.
        assert CheckoutSolution().checkout("K") == 70
        assert CheckoutSolution().checkout("KK") == 120
        # 3K: best is 2K for 120 plus a single K: 120 + 70 = 190.
        assert CheckoutSolution().checkout("KKK") == 190

    def test_new_product_P_offer(self):
        # P: price 50; Offer: 5P for 200.
        assert CheckoutSolution().checkout("P" * 5) == 200
        # 3P at full price:
        assert CheckoutSolution().checkout("P" * 3) == 150

    def test_new_product_Q_offer(self):
        # Q: price 30; Offer: 3Q for 80.
        assert CheckoutSolution().checkout("Q") == 30
        assert CheckoutSolution().checkout("Q" * 3) == 80
        # 4Q: apply offer once (80) plus one Q at full price (30): 80 + 30 = 110.
        assert CheckoutSolution().checkout("Q" * 4) == 110

    def test_new_product_V_offer(self):
        # V: price 50; Offers: 3V for 130 and 2V for 90.
        assert CheckoutSolution().checkout("V") == 50
        # 2V: offer 2V for 90.
        assert CheckoutSolution().checkout("VV") == 90
        # 3V: offer 3V for 130.
        assert CheckoutSolution().checkout("VVV") == 130
        # 4V: best is 2V for 90 + 2V for 90 = 180.
        assert CheckoutSolution().checkout("VVVV") == 180

    def test_new_product_U_offer(self):
        # U: price 40; Offer: For every 4 U's, pay for 3 (i.e. 3U free 1).
        assert CheckoutSolution().checkout("U") == 40
        # 4U: pay for 3*40 = 120.
        assert CheckoutSolution().checkout("UUUU") == 120
        # 5U: pay for 4, 1 free from 4 -> 4*40
        assert CheckoutSolution().checkout("UUUUU") == 160  # 5U: pay for 4, 1 free from 4 -> 4*40

    def test_new_product_N_M_cross_offer(self):
        # N: price 40; M: price 15; Offer: 3N get one M free.
        # Without M: "NNN" yields 3*40 = 120.
        assert CheckoutSolution().checkout("NNN") == 120
        # With one M: "NNNM", one M is free, so total = 3N * 40 + 15 = 135.
        assert CheckoutSolution().checkout("NNNM") == 135
        # With extra M's: "NNNNNNMM" -> 6N yield 6*40 = 240, and 6N gives two free Ms, so even if 2 M's are present, they are free.
        assert CheckoutSolution().checkout("NNNNNNMM") == 270  # 6N, 2M; 2 free Ms, no discount applied to cost

    def test_new_product_R_Q_cross_offer(self):
        # R: price 50; Q: price 30; Offer: 3R get one Q free.
        # "RRR" alone: 150.
        assert CheckoutSolution().checkout("RRR") == 150
        # "RRRQ": Q becomes free so total = 150.
        assert CheckoutSolution().checkout("RRRQ") == 180
        # "RRRQ" + extra Q: "RRRQQ" => free one Q, so pay for one Q: 150 + 30 = 210  # RRR = 150, Q=2 after 1 free, 1 paid
        assert CheckoutSolution().checkout("RRRQ" + "Q") == 210  # RRR = 150, Q=2 after 1 free, 1 paid

    def test_new_products_no_offer(self):
        # Test products that have no special offers.
        # I: 35, J: 60, L: 90, O: 10, S: 20, T: 20, W: 20, X: 17, Y: 20, Z: 21, G: 20.
        for sku, price in zip("IJLOSTWXYZG", [35, 60, 90, 10, 20, 20, 20, 17, 20, 21, 20]):
            assert CheckoutSolution().checkout(sku) == price

    def test_complex_basket_new_offers(self):
        # Construct a complex basket including multiple products:
        # For example, basket:
        basket = "AAAAABBEEFFFHHHHHHHHHHKKUUUUVVVVPPPQQQ"
        # Expected calculation:
        # A: 5A = 200
        # B: 2B, but note "EE" gives one free B. If there were any B's, reduce count. Here initial B count: 2; free B = (2E)//2 = 1; effective B = 2-1 = 1 * 30 = 30
        # E: 2E = 80
        # F: 3F, pay for 2 = 20
        # H: 10H = 80
        # K: 2K = 120
        # U: 4U, pay for 3 = 120
        # V: 4V = 180
        # P: 3P at full price = 150 (offer not triggered)
        # Q: 3Q = 80 (offer triggered for Q, but need exactly 3 for offer)
        expected = 200 + 30 + 80 + 20 + 80 + 120 + 120 + 180 + 150 + 80
        assert CheckoutSolution().checkout(basket) == expected

    def test_chk_r5_060(self):
        # 2E should make 1B free, so 40+40 = 80, B = free
        assert CheckoutSolution().checkout("EEB") == 80

    def test_chk_r5_061(self):
        # 3E = 1B free from 2E, remaining E + B = 40 + 40 + 30 = 110, minus free B (30) = 120
        assert CheckoutSolution().checkout("EEEB") == 120

    def test_chk_r5_062(self):
        # 4E = 2B free, 2B present, so both free: 4E = 160
        assert CheckoutSolution().checkout("EEEEBB") == 160
