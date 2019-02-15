import abc

class CoffeeCreator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def coffee_factory(self):
        pass
    
    def serve_coffee(self):
        product = self.coffee_factory()
        result = f"CoffeeCreator: The same coffee creator's code has just worked {product.make_coffee()}"
        return result

class CappuchinoCreator(CoffeeCreator):
    def coffee_factory(self) :
        return Cappuchino()

class MochaCreator(CoffeeCreator):
    def coffee_factory(self):
        return Mocha()


class Coffee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_coffee(self):
        pass

class Cappuchino(Coffee):
    def make_coffee(self):
        return "{Here's your cappuchino!!}"

class Mocha(Coffee):
    def make_coffee(self):
        return "{Here's your mocha!!}"

def coffee_client_code(creator: CoffeeCreator):
    print(f"Client: I'm not aware of the creator's class but it still works.\n")
    print(f"{creator.serve_coffee()}")

if __name__ == "__main__":
    print("App: Launched with cappuchino creator.")
    coffee_client_code(CappuchinoCreator())
    print("\n")
    
    print("App: Launched with mocha creator.")
    coffee_client_code(MochaCreator())

