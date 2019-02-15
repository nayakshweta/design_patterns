from abc import ABCMeta, abstractmethod

class AbstractUtensilFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_bowl(self):
        pass

    @abstractmethod
    def create_pan(self):
        pass

class PlasticUtensilFactory(AbstractUtensilFactory):

    def create_bowl(self):
        return plastic_bowl()
    
    def create_pan(self):
        return plastic_pan()

class SteelUtensilFactory(AbstractUtensilFactory):

    def create_bowl(self):
        return steel_bowl()
    
    def create_pan(self):
        return steel_pan()


class bowl(metaclass=ABCMeta):
    @abstractmethod
    def bowl_maker(self):
        pass

class plastic_bowl(bowl):
    def bowl_maker(self):
        print("Here's a plastic bowl")
        pass

class steel_bowl(bowl):
    def bowl_maker(self):
        print("Here's a steel bowl")
        pass


class pan(metaclass=ABCMeta):
    @abstractmethod
    def pan_maker(self):
        pass

class plastic_pan(pan):
    def pan_maker(self):
        print("Here's a plastic pan")
        pass

class steel_pan(pan):
    def pan_maker(self):
        print("Here's a steel pan")
        pass

def main():
    for utensilfactory in (PlasticUtensilFactory(),SteelUtensilFactory()):
        bowl = utensilfactory.create_bowl()
        pan = utensilfactory.create_pan()
        bowl.bowl_maker()
        pan.pan_maker()

if __name__ == "__main__":
    main()



