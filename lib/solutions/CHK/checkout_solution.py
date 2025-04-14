from collections import Counter

ERROR_CODE = -1

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

OFFERS = {
    "A": (3, 130),  # 3 A's for 130
    "B": (2, 45),   # 2 B's for 45
}


class CheckoutSolution:

    @staticmethod
    def _validate_skus(skus: list[str]) -> bool:
        # Validate if skus is a list of strings
        if not skus or not isinstance(skus, list) or not all(isinstance(sku, str) for sku in skus):
            return False
        return True

    # skus = unicode string
    def checkout(self, skus: list[str]) -> int:
        if not self._validate_skus(skus):
            return ERROR_CODE
        total = 0
        sku_count = Counter(skus)

        for sku, count in sku_count.items():
            if sku not in PRICES:
                return ERROR_CODE

            # Add remaining items at normal price
            total += count * PRICES[sku]

        return total





