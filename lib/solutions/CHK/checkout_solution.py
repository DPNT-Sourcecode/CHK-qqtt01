ERROR_CODE = -1


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



