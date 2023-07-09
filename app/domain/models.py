from __future__ import annotations

import secrets
import string


def sn_alphanum(length: int = 10) -> str:
    return "".join(secrets.choice(string.ascii_uppercase + string.digits[1:]) for i in range(length))


def generate_product_serial_number():
    return "PDT-" + sn_alphanum()


class Product:
    def __init__(self, title: str, quantity: int, price: int, sn: str | None = None):
        self.title = title
        self.quantity = quantity
        self.price = price
        self.product_serial_number = generate_product_serial_number()

    @property
    def get_total_price(self) -> int:
        return self.quantity * self.price

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return False
        return self.product_serial_number == other.product_serial_number

    def __hash__(self):
        return hash(self.product_serial_number)
