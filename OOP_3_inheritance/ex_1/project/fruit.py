from OOP_3_inheritance.ex_1.project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
