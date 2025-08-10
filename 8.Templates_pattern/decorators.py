from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

class Espresso(Coffee):
    def get_cost(self):
        return 20
    