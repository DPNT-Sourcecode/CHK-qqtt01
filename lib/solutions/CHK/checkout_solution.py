from collections import Counter

ERROR_CODE = -1

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

OFFERS = {
    "A": [(5, 200), (3, 130)],  # Offers for A: 5A for 200, 3A for 130
    "B": [(2, 45)],             # Offers for B: 2B for 45
    "H": [(10, 80), (5, 45)],    # Offers for H: 10H for 80, 5H for 45
    "K": [(2, 120)],            # Offers for K: 2K for 120
    "P": [(5, 200)],            # Offers for P: 5P for 200
    "Q": [(3, 80)],             # Offers for Q: 3Q for 80
    "V": [(3, 130), (2, 90)],    # Offers for V: 3V for 130, 2V for 90
    "U": [(4, 120)],            # Offers for U: 4U for 120 (3U get one U free)
}


GROUP_OFFERS = {
    ("S", "T", "X", "Y", "Z"): [(3, 45)],  # Offers for S, T, X, Y, Z: 3 for 45
}

class CheckoutSolution:

    @staticmethod
    def _validate_skus(skus: str) -> bool:
        # Validate that skus is a string containing only alphabetic characters
        if not isinstance(skus, str):
            return False
        return True

    def checkout(self, skus: str) -> int:
        if not self._validate_skus(skus):
            return ERROR_CODE
        total = 0
        sku_count = Counter(skus)

        def apply_buy_product_get_other_free(count, sku, free_sku = None):
            if free_sku is None:
                free_sku = sku
            if sku in sku_count and free_sku in sku_count:
                num_free = sku_count[sku] // count
                sku_count[free_sku] = max(0, sku_count[free_sku] - num_free)

        apply_buy_product_get_other_free(2, "E", "B")
        apply_buy_product_get_other_free(2, "F")

        # Apply 3N get one M free
        if "N" in sku_count and "M" in sku_count:
            num_free_m = sku_count["N"] // 3
            sku_count["M"] = max(0, sku_count["M"] - num_free_m)

        # Apply 3R get one Q free
        if "R" in sku_count and "Q" in sku_count:
            num_free_q = sku_count["R"] // 3
            sku_count["Q"] = max(0, sku_count["Q"] - num_free_q)


        # Main pricing loop
        for sku, count in sku_count.items():
            if sku not in PRICES:
                return ERROR_CODE

            # # Apply group offers if available
            # for group, offers in GROUP_OFFERS.items():
            #     if sku in group:
            #         for offer_qty, offer_price in sorted(offers, reverse=True):
            #             num_offers = count // offer_qty
            #             total += num_offers * offer_price
            #             count %= offer_qty

            # Apply special offers if available, sorted in descending order by quantity
            if sku in OFFERS:
                for offer_qty, offer_price in sorted(OFFERS[sku], reverse=True):
                    num_offers = count // offer_qty
                    total += num_offers * offer_price
                    count %= offer_qty

            # Add remaining items at normal price
            total += count * PRICES[sku]

        return total
