from solutions.CHK.checkout_solution import CheckoutSolution, PRICES as P, OFFERS as O, ERROR_CODE
from pytest import mark

@mark.parametrize("skus, expected", [
    ("", 0),
    ("123", ERROR_CODE),
    (None, ERROR_CODE),
    ("a", ERROR_CODE),
    (" A", ERROR_CODE),
    ("A", P["A"]),
    ("B", P["B"]),
    ("C", P["C"]),
    ("D", P["D"]),
    ("E", P["E"]),
    ("F", P["F"]),
    ("G", P["G"]),
    ("H", P["H"]),
    ("I", P["I"]),
    ("J", P["J"]),
    ("K", P["K"]),
    ("L", P["L"]),
    ("M", P["M"]),
    ("N", P["N"]),
    ("O", P["O"]),
    ("P", P["P"]),
    ("Q", P["Q"]),
    ("R", P["R"]),
    ("S", P["S"]),
    ("T", P["T"]),
    ("U", P["U"]),
    ("V", P["V"]),
    ("W", P["W"]),
    ("X", P["X"]),
    ("Y", P["Y"]),
    ("Z", P["Z"]),
    ("AA", P["A"] * 2),
    ("ABCD", P["A"] + P["B"] + P["C"] + P["D"]),
    ("AAA", O["A"][3]),  # 3A for 130
    ("AAAA", O["A"][3] + P["A"]),
    ("AAAAA", O["A"][5]),
    ("A" * 6, O["A"][5] + P["A"]), #5A for 200, 1A for 50
    ("A" * 7, O["A"][5] + P["A"] * 2),
    ("A" * 8, O["A"][5] + O["A"][3]),
    ("A" * 9, O["A"][5] + O["A"][3] + P["A"]),
    ("A" * 10, O["A"][5] * 2),
    ("BB", O["B"][2]),
    ("BBB", O["B"][2] + P["B"]),
    ("BBBB", O["B"][2] * 2),
    ("CC", P["C"] * 2),
    ("DD", P["D"] * 2),
    #  2E gets 1B free. Not applicable: 2B for 45.
    ("ABCDEABCDE", P["B"] * 2 + P["A"] * 2 + P["C"] * 2 + P["D"] * 2 + P["E"] * 2 - P["B"]),
    ("CCADDEEBBA", 2*P["C"] + P["A"] + 2*P["D"] + 2*P["E"] - P["B"] + 2*P["B"] + P["A"]),
    ("AAAAAEEBAAABB", O["A"][5] + 2*P["E"] - P["B"] + P["B"] + O["A"][3] + O["B"][2]),
    ("FF", P["F"]),
    ("FFF", P["F"] * 2),
    ("FFFF", P["F"] * 3),
    ("FFFFFF", P["F"] * 4),
    # 9A, 5B, 3C, 1D, 3E
    ("ABCDECBAABCABBAAAEEAA", (O["A"][5] + O["A"][3] + P["A"]) + (P["B"] + 2 * O["B"][2]) + 3 * P["C"] + P["D"] + (3 * P["E"] - P["B"])),

])
def test_checkout_solution(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected

#
# class TestCheckoutSolution:
#     def test_invalid_input(self):
#         assert CheckoutSolution().checkout("") == 0
#         assert CheckoutSolution().checkout("123") == -1
#         assert CheckoutSolution().checkout(None) == -1
#
#     def test_checkout_each(self):
#         assert CheckoutSolution().checkout("A") == 50
#         assert CheckoutSolution().checkout("B") == 30
#         assert CheckoutSolution().checkout("C") == 20
#         assert CheckoutSolution().checkout("D") == 15
#         assert CheckoutSolution().checkout("E") == 40
#         assert CheckoutSolution().checkout("F") == 10
#
#     def test_multiple_product(self):
#         assert CheckoutSolution().checkout("AA") == 100
#         assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
#
#     def test_discounts(self):
#         assert CheckoutSolution().checkout("AAA") == 130
#         assert CheckoutSolution().checkout("A" * 6) == 200 + 50
#         assert CheckoutSolution().checkout("BB") == 45
#         assert CheckoutSolution().checkout("BBBB") == 45 * 2
#
#     def test_product_have_no_discount(self):
#         assert CheckoutSolution().checkout("CC") == 40
#         assert CheckoutSolution().checkout("DD") == 30
#
#     def test_2es_gives_1b_free(self):
#         assert CheckoutSolution().checkout("EEB") == 80
#
#     def test_2e_no_b_to_discount(self):
#         # 2E without B still charges 2E only
#         assert CheckoutSolution().checkout("EE") == 80
#
#     def test_e_and_multiple_b_discount_limited(self):
#         # 2E can remove only one B
#         assert CheckoutSolution().checkout("EEBBB") == 40 + 40 + 45
#
#     def test_odd_number_of_es_and_bs(self):
#         # 5E gives 2B free, 1E no additional effect
#         assert CheckoutSolution().checkout("EEEEE" + "BBB") == 40 * 5 + 30
#
#     def test_discount_priority_on_a(self):
#         # 5A should apply 5A for 200, not 3A+2A
#         assert CheckoutSolution().checkout("A" * 5) == 200
#
#     def test_mixed_items_with_all_discounts(self):
#         # 5A (200), 2B (80), 2E (1B free), 1B charged 30
#         assert CheckoutSolution().checkout("AAAAABBEE") == 200 + 80 + 30
#
#     def test_f_offer_exactly_three(self):
#         # F: price 10; Offer: 3F for 20.
#         assert CheckoutSolution().checkout("F" * 2) == 20
#
#     def test_f_offer_with_remainder(self):
#         assert CheckoutSolution().checkout("F" * 4) == 40
#
#     def test_f_offer_multiple_sets(self):
#         assert CheckoutSolution().checkout("F" * 5) == 50
#
#     def test_new_product_H_offers(self):
#         # H: price 10; Offers: 5H for 45 and 10H for 80.
#         # 5 H's should yield 45.
#         assert CheckoutSolution().checkout("H" * 5) == 45
#         # 10 H's should yield 80.
#         assert CheckoutSolution().checkout("H" * 10) == 80
#         # 7 H's: best is using the 5H offer for 45, then 2 at full price: 45 + 20 = 65.
#         assert CheckoutSolution().checkout("H" * 7) == 65
#
#     def test_new_product_K_offer(self):
#         # K: price 70; Offer: 2K for 120.
#         assert CheckoutSolution().checkout("K") == 70
#         assert CheckoutSolution().checkout("KK") == 120
#         # 3K: best is 2K for 120 plus a single K: 120 + 70 = 190.
#         assert CheckoutSolution().checkout("KKK") == 190
#
#     def test_new_product_P_offer(self):
#         # P: price 50; Offer: 5P for 200.
#         assert CheckoutSolution().checkout("P" * 5) == 200
#         # 3P at full price:
#         assert CheckoutSolution().checkout("P" * 3) == 150
#
#     def test_new_product_Q_offer(self):
#         # Q: price 30; Offer: 3Q for 80.
#         assert CheckoutSolution().checkout("Q") == 30
#         assert CheckoutSolution().checkout("Q" * 3) == 80
#         # 4Q: apply offer once (80) plus one Q at full price (30): 80 + 30 = 110.
#         assert CheckoutSolution().checkout("Q" * 4) == 110
#
#     def test_new_product_V_offer(self):
#         # V: price 50; Offers: 3V for 130 and 2V for 90.
#         assert CheckoutSolution().checkout("V") == 50
#         # 2V: offer 2V for 90.
#         assert CheckoutSolution().checkout("VV") == 90
#         # 3V: offer 3V for 130.
#         assert CheckoutSolution().checkout("VVV") == 130
#         # 4V: best is 2V for 90 + 2V for 90 = 180.
#         assert CheckoutSolution().checkout("VVVV") == 180
#
#     def test_new_product_U_offer(self):
#         # U: price 40; Offer: For every 4 U's, pay for 3 (i.e. 3U free 1).
#         assert CheckoutSolution().checkout("U") == 40
#         # 4U: pay for 3*40 = 120.
#         assert CheckoutSolution().checkout("UUUU") == 120
#         # 5U: pay for 4, 1 free from 4 -> 4*40
#         assert CheckoutSolution().checkout("UUUUU") == 160  # 5U: pay for 4, 1 free from 4 -> 4*40
#
#     def test_new_product_N_M_cross_offer(self):
#         # N: price 40; M: price 15; Offer: 3N get one M free.
#         # Without M: "NNN" yields 3*40 = 120.
#         assert CheckoutSolution().checkout("NNN") == 120
#         # With one M: "NNNM", one M is free, so total = 3N * 40 + 15 = 135.
#         assert CheckoutSolution().checkout("NNNM") == 120
#         # With extra M's: "NNNNNNMM" -> 6N yield 6*40 = 240, and 6N gives two free Ms, so even if 2 M's are present, they are free.
#         assert CheckoutSolution().checkout("NNNNNNMM") == 240  # 6N, 2M; 2 free Ms, no discount applied to cost
#
#     def test_new_product_R_Q_cross_offer(self):
#         # R: price 50; Q: price 30; Offer: 3R get one Q free.
#         # "RRR" alone: 150.
#         assert CheckoutSolution().checkout("RRR") == 150
#         # "RRRQ": Q becomes free so total = 150.
#         assert CheckoutSolution().checkout("RRRQ") == 150
#         # "RRRQ" + extra Q: "RRRQQ" => free one Q, so pay for one Q: 150 + 30 = 210  # RRR = 150, Q=2 after 1 free, 1 paid
#         assert CheckoutSolution().checkout("RRRQ" + "Q") == 150 + 30  # RRR = 150, Q=2 after 1 free, 1 paid
#
#     def test_new_products_no_offer(self):
#         # Test products that have no special offers.
#         # I: 35, J: 60, L: 90, O: 10, S: 20, T: 20, W: 20, X: 17, Y: 20, Z: 21, G: 20.
#         for sku, price in zip("IJLOSTWXYZG", [35, 60, 90, 10, 20, 20, 20, 17, 20, 21, 20]):
#             assert CheckoutSolution().checkout(sku) == price
#
#     def test_chk_r5_060(self):
#         # 2E should make 1B free, so 40+40 = 80, B = free
#         assert CheckoutSolution().checkout("EEB") == 80
#
#     def test_chk_r5_061(self):
#         # 3E = 1B free from 2E, remaining E + B = 40 + 40 + 30 = 110, minus free B (30) = 120
#         assert CheckoutSolution().checkout("EEEB") == 120
#
#     def test_chk_r5_062(self):
#         # 4E = 2B free, 2B present, so both free: 4E = 160
#         assert CheckoutSolution().checkout("EEEEBB") == 160
#
#     def test_3S_group_offer(self):
#         # Buy any 3 of (S, T, X, Y, Z) for 45.
#         # 3S = 60, 3T = 60, 3X = 51, 3Y = 60, 3Z = 63
#         assert CheckoutSolution().checkout("SSS") == 45
#         assert CheckoutSolution().checkout("SS") == 40
#
#     def test_3T_group_offer(self):
#         assert CheckoutSolution().checkout("TTT") == 45
#         assert CheckoutSolution().checkout("TT") == 40
#
#     def test_STX_group_offer(self):
#         # 3S + 3T + 3X = 45 + 45 + 51 = 141
#         assert CheckoutSolution().checkout("STX") == 45
