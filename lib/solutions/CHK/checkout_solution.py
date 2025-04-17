from collections import defaultdict

from solutions.CHK.constants import (
    ERROR_CODE,
    PRICES,
    OFFERS,
    GROUP_SKUS,
    GROUP_PRICE,
    GROUP_SIZE,
    CROSS_ITEM_OFFERS, SAME_ITEM_OFFERS,
)
from solutions.CHK.exceptions import InvalidSKUError


class CheckoutSolution:
    @staticmethod
    def _validate_skus(skus: str) -> bool:

        # Validate that skus is a string containing only alphabetic characters
        if not isinstance(skus, str):
            return False
        return True

    def __init__(self):
        self.total = 0
        self.group_items = []
        self.sku_count = defaultdict(int)

    def count_skus(self, skus: str) -> None:
        """Count the number of each SKU in the input string.

        Args:
            skus (str): A string of SKUs in the form "ABDFDFS"
        Returns:
            None
        Raises:
            InvalidSKUError: If any SKU is invalid

        """
        if self.sku_count:
        for s in skus:
            if s not in PRICES:
                raise InvalidSKUError(s)

            # Extract group items into separate structure
            if s in GROUP_SKUS:
                self.group_items.append(s)
            else:
                # Count the number of each SKU
                self.sku_count[s] += 1

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

        # Apply cross-item offers
        def apply_buy_product_get_other_free(
            num: int, sku: str, free_sku: str | None = None
        ):
            if free_sku is None:
                free_sku = sku
            if sku in sku_count and free_sku in sku_count and sku_count[sku] >= num:
                sku_num = 1
                while sku_num < sku_count[sku] and sku_count[free_sku] > 0:
                    sku_count[free_sku] = max(0, sku_count[free_sku] - 1)
                    if free_sku == sku:
                        sku_num += 1
                    sku_num += num

        for offer in CROSS_ITEM_OFFERS:
            apply_buy_product_get_other_free(
                offer.min_count, offer.sku, offer.free_sku
            )

        # Apply same-item offers
        for offer in SAME_ITEM_OFFERS:
            if offer.sku in sku_count:
                count = sku_count[offer.sku]
                free = count // offer.min_count
                sku_count[offer.sku] -= free

        # Handle remaining items
        for sku, count in sku_count.items():

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

