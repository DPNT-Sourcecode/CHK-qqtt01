from collections import OrderedDict

from solutions.CHK.models import FreeOffer

ERROR_CODE = -1
PRICES: dict[str: int] = {
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
OFFERS: dict[str: OrderedDict] = {
    "A": OrderedDict({5: 200, 3: 130}),  # 5A for 200, 3A for 130
    "B": OrderedDict({2: 45}),  # 2B for 45
    "H": OrderedDict({10: 80, 5: 45}),  # 10H for 80, 5H for 45
    "K": OrderedDict({2: 120}),  # 2K for 120
    "P": OrderedDict({5: 200}),  # 5P for 200
    "Q": OrderedDict({3: 80}),  # 3Q for 80
    "V": OrderedDict({3: 130, 2: 90}),  # 3V for 130, 2V for 90
}

# Free items offers
FREE_OFFERS: list[FreeOffer] = [
    FreeOffer(sku="E", min_count=2, free_sku="B"),  # 2E gets 1B free,
    FreeOffer(sku="F", min_count=2),  # 2F gets 1F free
    FreeOffer(sku="N", min_count=3, free_sku="M"),  # 3N gets 1M free
    FreeOffer(sku="R", min_count=2, free_sku="Q"),  # 2R gets 1Q free
    FreeOffer(sku="U", min_count=3),  # 3U gets 1U free
]

GROUP_SKUS = {"S", "T", "X", "Y", "Z"}
GROUP_PRICE = 45
GROUP_SIZE = 3

