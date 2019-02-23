import abc

class AbstractObject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass
    
class RealObject(AbstractObject):
    def request(self):
        print("Do something")
        pass

class NullObject(AbstractObject):
    def request(self):
        pass