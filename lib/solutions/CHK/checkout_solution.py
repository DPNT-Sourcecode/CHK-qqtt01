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
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

OFFERS = {
    "A": [(3, 130), (5, 200)],  # Offers for A: 3A for 130, 5A for 200
    "B": [(2, 45)],             # Offers for B: 2B for 45
    "H": [(10, 80), (5, 45)],    # Offers for H: 10H for 80, 5H for 45
    "K": [(2, 150)],            # Offers for K: 2K for 150
    "P": [(5, 200)],            # Offers for P: 5P for 200
    "Q": [(3, 80)],             # Offers for Q: 3Q for 80
    "V": [(3, 130), (2, 90)],    # Offers for V: 3V for 130, 2V for 90
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

        # Apply cross-item free offers:
        # 2E get one B free
        if "E" in sku_count and "B" in sku_count:
            num_es = sku_count["E"]
            num_bs = sku_count["B"]
            free_bs = num_es // 2
            sku_count["B"] = max(0, num_bs - free_bs)

        # 3N get one M free
        if "N" in sku_count and "M" in sku_count:
            num_ns = sku_count["N"]
            num_ms = sku_count["M"]
            free_ms = num_ns // 3
            sku_count["M"] = max(0, num_ms - free_ms)

        # 3R get one Q free
        if "R" in sku_count and "Q" in sku_count:
            num_rs = sku_count["R"]
            num_qs = sku_count["Q"]
            free_qs = num_rs // 3
            sku_count["Q"] = max(0, num_qs - free_qs)

        # Apply F discount: For every 3 F's, 1 is free (i.e., pay for 2)
        if "F" in sku_count:
            count_f = sku_count["F"]
            sku_count["F"] = count_f - (count_f // 3)

        # Apply U discount: For every 4 U's, pay for 3 (i.e., 3U get one U free)
        if "U" in sku_count:
            count_u = sku_count["U"]
            sku_count["U"] = count_u - (count_u // 4)

        # Main pricing loop
        for sku, count in sku_count.items():
            if sku not in PRICES:
                return ERROR_CODE

            # Apply special offers if available, sorted in descending order by quantity
            if sku in OFFERS:
                for offer_qty, offer_price in sorted(OFFERS[sku], reverse=True):
                    num_offers = count // offer_qty
                    total += num_offers * offer_price
                    count %= offer_qty

            # Add remaining items at normal price
            total += count * PRICES[sku]

        return total



