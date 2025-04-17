from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.constants import ERROR_CODE, PRICES as P, OFFERS as O, GROUP_PRICE, GROUP_SKUS
from pytest import mark


@mark.parametrize(
    "skus, expected",
    [
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
        ("A" * 6, O["A"][5] + P["A"]),  # 5A for 200, 1A for 50
        ("A" * 7, O["A"][5] + P["A"] * 2),
        ("A" * 8, O["A"][5] + O["A"][3]),
        ("A" * 9, O["A"][5] + O["A"][3] + P["A"]),
        ("A" * 10, O["A"][5] * 2),
        ("BB", O["B"][2]),
        ("BBB", O["B"][2] + P["B"]),
        ("BBBB", O["B"][2] * 2),
        ("BBBBB", O["B"][2] * 2 + P["B"]),
        ("CC", P["C"] * 2),
        ("DD", P["D"] * 2),
        ("EE", P["E"] * 2),
        ("EEB", P["E"] * 2),  # B is free
        ("EEEB", P["E"] * 3),
        ("EEEBB", P["E"] * 3 + P["B"]),  # 1B is free
        ("EEEEBB", P["E"] * 4),  # 2B free
        ("BEBEEE", P["E"] * 4),  # B free
        #  2E gets 1B free. Not applicable: 2B for 45.
        (
            "ABCDEABCDE",
            P["B"] * 2 + P["A"] * 2 + P["C"] * 2 + P["D"] * 2 + P["E"] * 2 - P["B"],
        ),
        (
            "CCADDEEBBA",
            2 * P["C"]
            + P["A"]
            + 2 * P["D"]
            + 2 * P["E"]
            - P["B"]
            + 2 * P["B"]
            + P["A"],
        ),
        (
            "AAAAAEEBAAABB",
            O["A"][5] + 2 * P["E"] - P["B"] + P["B"] + O["A"][3] + O["B"][2],
        ),
        ("FF", P["F"] * 2),
        ("FFF", P["F"] * 2),
        ("FFFF", P["F"] * 3),
        ("FFFFFF", P["F"] * 4),
        # 9A, 5B, 3C, 1D, 3E
        (
            "ABCDECBAABCABBAAAEEAA",
            (O["A"][5] + O["A"][3] + P["A"])
            + (P["B"] + 2 * O["B"][2])
            + 3 * P["C"]
            + P["D"]
            + (3 * P["E"] - P["B"]),
        ),
        # 5H for 45, 10H for 80
        ("H" * 5, O["H"][5]),
        ("H" * 10, O["H"][10]),
        ("H" * 7, O["H"][5] + P["H"] * 2),
        ("H" * 20, O["H"][10] * 2),
        # 2K for 120
        ("K" * 2, O["K"][2]),
        # 3N get one M free
        ("NNNM", P["N"] * 3),
        ("NNNMM", P["N"] * 3 + P["M"]),
        ("NNNNNNMM", P["N"] * 6),
        # 5P for 200
        ("P" * 5, O["P"][5]),
        # 3Q for 80
        ("Q" * 3, O["Q"][3]),
        ("Q" * 4, O["Q"][3] + P["Q"]),
        # 3R get one Q free
        ("RRQ", P["R"] * 2 + P["Q"]),  # no discount
        ("RRRQ", P["R"] * 3),
        ("RRRQQ", P["R"] * 3 + P["Q"]),
        # 3U get one U free
        ("UU", P["U"] * 2),  # no discount
        ("UUU", P["U"] * 3),
        ("UUUU", P["U"] * 3),
        ("UUUUU", P["U"] * 4),
        # 2V for 90, 3V for 130
        ("VV", O["V"][2]),
        ("VVV", O["V"][3]),
        ("VVVV", O["V"][2] * 2),
        ("VVVVV", O["V"][3] + O["V"][2]),
        ("V" * 6, O["V"][3] * 2),
        # buy any 3 of (S,T,X,Y,Z) for 45 (GROUP_PRICE)
        ("STXYZ", GROUP_PRICE + P["X"] + P["Y"]),
        ("STXYZ" * 2, GROUP_PRICE * 3 + P["X"]),
        ("STXYZTSTYZXSTYXZYTSYTZXYT", 8 * GROUP_PRICE + P["X"]),
        ("SS", 2 * P["S"]),
        ("SSS", GROUP_PRICE),
        ("TTT", GROUP_PRICE),
        ("XXX", GROUP_PRICE),
        ("YYY", GROUP_PRICE),
        ("ZZZ", GROUP_PRICE),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", sum(v for k, v in P.items() if k not in GROUP_SKUS) + GROUP_PRICE + P["X"] + P["Y"]),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", 1602),
    ],
)
def test_checkout_solution(skus, expected):
    assert CheckoutSolution().checkout(skus) == expected




