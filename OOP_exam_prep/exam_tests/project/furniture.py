from typing import Tuple, Optional


class Furniture:
    def __init__(self,
                 model: str,
                 price: float,
                 dimensions: Tuple[int, int, int],
                 in_stock: bool = True,
                 weight: Optional[float] = None):
        self.model = model
        self.price = price
        self.dimensions = dimensions
        self.in_stock = in_stock
        self.weight = weight

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value.strip() or len(value.strip()) > 50:
            raise ValueError("Model must be a non-empty string with a maximum length of 50 characters.")
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not value >= 0.0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        if not len(value) == 3:
            raise ValueError("Dimensions tuple must contain 3 integers.")
        if any(size <= 0 for size in value):
            raise ValueError("Dimensions tuple must contain integers greater than zero.")
        self._dimensions = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value is not None and value <= 0.0:
            raise ValueError("Weight must be greater than zero.")
        self._weight = value

    def get_available_status(self):
        return (f"Model: {self._model} is currently "
                f"{'in stock' if self.in_stock else 'unavailable'}.")

    def get_specifications(self):
        height, width, depth = self.dimensions
        weight = self.weight if self.weight is not None else 'N/A'
        return (f"Model: {self.model} has the following dimensions: "
                f"{height}mm x {width}mm x {depth}mm and weighs: {weight}")
