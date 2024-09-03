from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def increase_stock(self, stock_to_add: int):
        self.check_positive_number(stock_to_add)
        self.stock += stock_to_add

    def decrease_stock(self, stock_to_reduce: int):
        self.check_positive_number(stock_to_reduce)  # Corrigido aqui
        new_stock = self.stock - stock_to_reduce
        self.check_negative_stock(new_stock)
        self.stock = new_stock  # Corrigido aqui

    def check_positive_number(self, value: int):  # Corrigido aqui
        if value <= 0:
            raise Exception("Number must be positive")

    def check_negative_stock(self, value: int):  # Corrigido aqui
        if value < 0:
            raise Exception("Stock must be greater than or equal to 0")
