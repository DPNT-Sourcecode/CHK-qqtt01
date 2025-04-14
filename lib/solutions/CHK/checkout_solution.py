from pydantic import BaseModel, constr

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        raise NotImplementedError()
