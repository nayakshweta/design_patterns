from datetime import datetime
from copy import deepcopy
from typing import Any

class Prototype:
    def __init__(self):
        self._primitive = None
        self._component = None
        self._circular_reference = None
    
    @property
    def primitive(self):
        return self._primitive

    @primitive.setter
    def primitive(self, value: Any):
        self._primitive = value
    
    @property
    def component(self):
        return self._component
    
    @component.setter
    def component(self, value: object):
        self._component = value

    @property
    def circular_reference(self):
        return self._circular_reference
    
    @circular_reference.setter
    def circular_reference(self, value):
        self._circular_reference = value
    
    def clone(self):

        self.component = deepcopy(self.component)
        self.circular_reference = deepcopy(self.circular_reference)
        self.circular_reference.prototype = self
        return deepcopy(self)


class ComponentWithBackReference:
    def __init__(self, prototype: Prototype):
        self.prototype = prototype

    @property
    def prototype(self):
        return self._prototype
    
    @prototype.setter
    def prototype(self, value: Prototype):
        self._prototype = value


if __name__ == "__main__":
    p1 = Prototype()
    p1.primitive = 245
    p1.component = datetime.now()
    p1.circular_reference = ComponentWithBackReference(p1)

    p2 = p1.clone()

    if p1.primitive is p2.primitive:
        print("Primitive field values have been carried over to a clone. Yay!")
    else:
        print("Primitive field values have not been copied. Booo!")
    
    if p1.component is p2.component:
        print("Simple component has not been cloned. Boo!")
    else:
        print("Simple component has been cloned. Yay!")
    
    if p1.circular_reference is p2.circular_reference:
        print("Component with backreference has not been cloned. Boo!")
    else:
        print("Component with backreference has been cloned. Yay!")
    
    if p1.circular_reference.prototype is p2.circular_reference.prototype:
        print("Component with backreference is linked to the original object. Boo!", end="")
    else:
        print("Component with backreference is linked to the clone. Yay!", end="")

