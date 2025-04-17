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
    """Checkout class to handle the checkout process and apply offers.

    """
    def __init__(self):
        self.total = 0
        self.group_items = []
        self.sku_count = defaultdict(int)

    @staticmethod
    def _validate_skus(skus: str) -> bool:

        # Validate that skus is a string containing only alphabetic characters
        if not isinstance(skus, str):
            raise InvalidSKUError(skus)
        return True

    def count_skus(self, skus: str) -> None:
        """Count the number of each SKU in the input string.

        Args:
            skus (str): A string of SKUs in the form "ABDFDFS"
        Returns:
            None
        Raises:
            InvalidSKUError: If any SKU is invalid

        """
        self._validate_skus(skus)
        for s in skus:
            # Extra validation to check if the SKU is valid
            if s not in PRICES:
                raise InvalidSKUError(s)

            # Extract group items into separate structure
            if s in GROUP_SKUS:
                self.group_items.append(s)
            else:
                # Count the number of each SKU
                self.sku_count[s] += 1

    def handle_group_items(self) -> None:
        """Handle group items and apply group offers.

        """
        # Sort them descending to discount the most expensive first
        sorted_group_items = sorted(self.group_items, key=lambda x: PRICES[x], reverse=True)
        while len(sorted_group_items) >= GROUP_SIZE:
            self.total += GROUP_PRICE
            # slice the head of the list removing counted GROUP_SIZE items
            sorted_group_items = sorted_group_items[GROUP_SIZE:]
        # Handle remaining group items
        for sku in sorted_group_items:
            self.total += PRICES[sku]

    def checkout(self, skus: str) -> int:
        """Calculate the total price of the items in the basket.

        Args:
            skus (str): A string of SKUs in the form "ABDFDFS"
        Returns:
            int: The total price of the items in the basket, or ERROR_CODE if invalid input

        """
        if not self._validate_skus(skus):
            return ERROR_CODE
        try:
            self.count_skus(skus)
        except InvalidSKUError as _e:
            return ERROR_CODE

        self.handle_group_items()
        # TODO(refactor): Remove this line after refactoring into instance methods
        sku_count = self.sku_count
        total = self.total

        self.apply_cross_item_offers()
        self.apply_same_item_offers()

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

    def apply_same_item_offers(self):
        """Apply same-item offers to the basket.

        """
        for offer in SAME_ITEM_OFFERS:
            if offer.sku in self.sku_count and self.sku_count[offer.sku] >= offer.min_count:
                count = self.sku_count[offer.sku]
                free = count // offer.min_count
                self.sku_count[offer.sku] -= free

    def apply_cross_item_offers(self):
        """Apply cross-item offers to the basket.

        """
        for offer in CROSS_ITEM_OFFERS:
            # Check if the offer is applicable
            if (offer.sku in self.sku_count
                and offer.free_sku in self.sku_count
                and self.sku_count[offer.sku] >= offer.min_count
            ):
                # Counting free items
                count = self.sku_count[offer.sku] // offer.min_count
                # Applying the offer keeping the free items valid, i.e. above 0
                self.sku_count[offer.free_sku] = max(0, self.sku_count[offer.free_sku] - count)


