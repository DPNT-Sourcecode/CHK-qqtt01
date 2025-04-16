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

from collections import OrderedDict


# Presorted offers for each SKU to implement largest offer first policy
OFFERS = {
    "A": OrderedDict({5: 200, 3: 130}), # 5A for 200, 3A for 130
    "B": OrderedDict({2: 45}),          # 2B for 45
    "H": OrderedDict({10: 80, 5: 45}),  # 10H for 80, 5H for 45
    "K": OrderedDict({2: 120}),         # 2K for 120
    "P": OrderedDict({5: 200}),         # 5P for 200
    "Q": OrderedDict({3: 80}),          # 3Q for 80
    "V": OrderedDict({3: 130, 2: 90}),  # 3V for 130, 2V for 90
}

GROUP = {"S", "T", "X", "Y", "Z"}
GROUP_PRICE = 45
GROUP_NUM = 3

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

        # # Handle group offers
        # group_count = sum([n for s, n in sku_count.items() if s in GROUP])
        # if group_count >= GROUP_NUM:
        #     total += (group_count // GROUP_NUM) * GROUP_PRICE
        #     for sku in GROUP:
        #         if sku in sku_count:
        #             sku_count[sku] = max(0, sku_count[sku] - group_count // GROUP_NUM * GROUP_NUM)

        # Handle special offers
        def apply_buy_product_get_other_free(num, sku, free_sku = None):
            if free_sku is None:
                free_sku = sku
            if sku in sku_count and free_sku in sku_count:
                num_free = sku_count[sku] // num
                sku_count[free_sku] = max(0, sku_count[free_sku] - num_free)

        apply_buy_product_get_other_free(2, "E", "B")
        apply_buy_product_get_other_free(2, "F")
        apply_buy_product_get_other_free(2, "N", "M")
        apply_buy_product_get_other_free(2, "R", "Q")
        apply_buy_product_get_other_free(3, "U")


        # Handle remaining items
        for sku, count in sku_count.items():
            if sku not in PRICES:
                return ERROR_CODE

            # Apply special offers if available, sorted in descending order by quantity
            # Assuming the policy is to apply the largest offer first
            if sku in OFFERS:
                for offer_qty, offer_price in OFFERS[sku].items():
                    num_offers = count // offer_qty
                    total += num_offers * offer_price
                    count %= offer_qty

            # Add remaining items at normal price
            total += count * PRICES[sku]

        return total


