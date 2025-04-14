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
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

OFFERS = {
    "A": [(3, 130), (5, 200)],  # Offers for A: 3A for 130, 5A for 200
    "B": [(2, 45)],             # Offers for B: 2B for 45
    "H": [(10, 80), (5, 45)],    # Offers for H: 10H for 80, 5H for 45
    "K": [(2, 120)],            # Offers for K: 2K for 120
    "P": [(5, 200)],            # Offers for P: 5P for 200
    "Q": [(3, 80)],             # Offers for Q: 3Q for 80
    "V": [(3, 130), (2, 90)],    # Offers for V: 3V for 130, 2V for 90
    "U": [(4, 120)],            # Offers for U: 4U for 120

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

        # Group discount offer: any 3 of (S,T,X,Y,Z) for 45
        group_skus = {"S", "T", "X", "Y", "Z"}
        group_items = []
        for sku in list(sku_count):
            if sku in group_skus:
                group_items.extend([sku] * sku_count[sku])
                del sku_count[sku]

        group_items.sort(key=lambda s: PRICES[s], reverse=True)
        group_discount = 0
        num_groups = len(group_items) // 3
        group_discount += num_groups * 45
        remaining = group_items[num_groups * 3:]
        group_discount += sum(PRICES[s] for s in remaining)
        total += group_discount

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


