
class Component():
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component = None

    def __init__(self, component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component
    
    def operation(self) -> str:
        self._component.operation()

class ConcreteDecoratorA(Decorator):

    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component) -> None:
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: I have got a simple component")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)