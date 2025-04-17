from collections import Counter, defaultdict

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

GROUP_SKUS = {"S", "T", "X", "Y", "Z"}
GROUP_PRICE = 45
GROUP_SIZE = 3

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
        group_items = []
        sku_count = defaultdict(int)
        for s in skus:
            if s not in PRICES:
                return ERROR_CODE

            # Extract group items into separate structure
            if s in GROUP_SKUS:
                group_items.append(s)
            else:
                # Count the number of each SKU
                sku_count[s] += 1

        # Handle group offers
        # Sort them descending to discount the most expensive first
        sorted_group_items = sorted(group_items, key=lambda x: PRICES[x], reverse=True)
        while len(sorted_group_items) >= GROUP_SIZE:
            total += GROUP_PRICE
            sorted_group_items = sorted_group_items[GROUP_SIZE:]
        # Handle remaining group items
        for sku in sorted_group_items:
            total += PRICES[sku]


        # Handle special offers
        def apply_buy_product_get_other_free(num, sku, free_sku = None):
            if free_sku is None:
                free_sku = sku
            if sku in sku_count and free_sku in sku_count and sku_count[sku] >= num:
                sku_num = 1
                while sku_num < sku_count[sku] and sku_count[free_sku] > 0:
                    sku_count[free_sku] = max(0, sku_count[free_sku] - 1)
                    if free_sku == sku:
                        sku_num += 1
                    sku_num += num

        apply_buy_product_get_other_free(2, "E", "B")
        apply_buy_product_get_other_free(2, "F")
        apply_buy_product_get_other_free(3, "N", "M")
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







