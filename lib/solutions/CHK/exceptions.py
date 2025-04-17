class InvalidSKUError(Exception):
    """Custom exception for invalid SKU input."""

    def __init__(self, sku):
        self.sku = sku
        super().__init__(f"Invalid SKU: {sku}")

class InvalidInputSKUFormatError(Exception):
    """Custom exception for invalid SKUs input format."""

    def __init__(self, skus):
        self.skus = skus
        super().__init__(f"Invalid SKUs format: {skus}")

