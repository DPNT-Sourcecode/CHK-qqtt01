class CheckoutSolution:

    def _validate_skus(self, skus):
        # Validate if skus is a list of strings
        if not isinstance(skus, list) or not all(isinstance(sku, str) for sku in skus):
            return False
        return True

    # skus = unicode string
    def checkout(self, skus: list[str]) -> int:

        return -1


