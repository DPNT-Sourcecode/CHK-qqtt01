from collections import Counter

ERROR_CODE = -1

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}

OFFERS = {
    "A": [(3, 130), (5, 200)],  # 3 A's for 130 5 A's for 200
    "B": [(2, 45)],   # 2 B's for 45

}


class CheckoutSolution:

    @staticmethod
    def _validate_skus(skus: str) -> bool:
        # Validate if skus is a list of strings
        if not isinstance(skus, str):
            return False
        return True

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._validate_skus(skus):
            return ERROR_CODE
        total = 0
        sku_count = Counter(skus)

        # Apply 2Es gives 1 B free
        num_es = sku_count.get('E', 0)
        num_bs = sku_count.get('B', 0)
        free_bs = num_es // 2
        sku_count['B'] = max(0, num_bs - free_bs)

        for sku, count in sku_count.items():
            if sku not in PRICES:
                return ERROR_CODE

            # Check for special F offer
            if sku == "F":
                free_fs = count // 3
                payable_fs = count - free_fs
                total += payable_fs * PRICES[sku]
                continue


            # Check for special offers
            if sku in OFFERS:
                # Apply offers
                for offer_qty, offer_price in sorted(OFFERS[sku], reverse=True):
                    num_offers = count // offer_qty
                    total += num_offers * offer_price
                    count %= offer_qty

            # Add remaining items at normal price
            total += count * PRICES[sku]

        return total



