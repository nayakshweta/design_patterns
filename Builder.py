from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):

    @abstractproperty
    def product(self):
        pass
    
    @abstractmethod
    def create_salad_parta_veggies(self):
        pass
    
    @abstractmethod
    def create_salad_partb_meat(self):
        pass
    
    @abstractmethod
    def create_salad_partc_nuts(self):
        pass
    
    @abstractmethod
    def create_salad_partd_dressing(self):
        pass

class SaladBuilder(Builder):

    def __init__(self):
        self.reset()
    
    def reset(self):
        self._product = Salad()
    
    @property
    def product(self):
        product = self._product
        self.reset()
        return product
    
    def create_salad_parta_veggies(self):
        self._product.add("Veggies")

    def create_salad_partb_meat(self):
        self._product.add("Meat")
    
    def create_salad_partc_nuts(self):
        self._product.add("Nuts")
    
    def create_salad_partd_dressing(self):
        self._product.add("Dressing")


class Salad():

    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)
    
    def list_ingredients(self):
        print(f"salad is made up of:{', '.join(self.parts)}", end="")

class Director():

    def __init__(self):
        self.builder = None
    
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder
    
    def build_basic_veg_salad(self):
        self.builder.create_salad_parta_veggies()
    
    def build_gourmet_salad(self):
        self.builder.create_salad_parta_veggies()
        self.builder.create_salad_partb_meat()
        self.builder.create_salad_partc_nuts()
        self.builder.create_salad_partd_dressing()

if __name__ == "__main__":
    director = Director()
    builder = SaladBuilder()
    director.builder = builder

    print("Basic Veg salad: ")
    director.build_basic_veg_salad()
    builder.product.list_ingredients()

    print("\n")

    print("Gourmet salad is the best!")
    director.build_gourmet_salad()
    builder.product.list_ingredients()

    print("\n")
    
    print("Custom product: ")
    builder.create_salad_parta_veggies()
    builder.create_salad_partd_dressing()
    builder.product.list_ingredients()

