class InvalidSKUError(Exception):
    """Custom exception for invalid SKU input."""

    def __init__(self, sku):
        self.sku = sku
        super().__init__(f"Invalid SKU: {sku}")
