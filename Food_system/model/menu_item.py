class MenuItem:
    def __init__(self, code: int, name: str, price: float):
        self._code = code
        self._name = name
        self._price = price

    @property
    def code(self):
        return self._code

    def set_code(self, c: str):
        self._code = c

    @property
    def name(self):
        return self._name

    def set_name(self, n: str):
        self._name = n

    @property
    def price(self):
        return self._price

    def set_price(self, p: float):
        self._price = p
