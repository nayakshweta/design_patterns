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
        return PlasticBowl()
    
    def create_pan(self):
        return PlasticPan()

class SteelUtensilFactory(AbstractUtensilFactory):

    def create_bowl(self):
        return SteelBowl()
    
    def create_pan(self):
        return SteelPan()


class Bowl(metaclass=ABCMeta):
    @abstractmethod
    def bowl_maker(self):
        pass

class PlasticBowl(Bowl):
    def bowl_maker(self):
        print("Here's a plastic bowl")
        pass

class SteelBowl(Bowl):
    def bowl_maker(self):
        print("Here's a steel bowl")
        pass


class Pan(metaclass=ABCMeta):
    @abstractmethod
    def pan_maker(self):
        pass

class PlasticPan(Pan):
    def pan_maker(self):
        print("Here's a plastic pan")
        pass

class SteelPan(Pan):
    def pan_maker(self):
        print("Here's a steel pan")
        pass

def main():
    for utensil_factory in (PlasticUtensilFactory(),SteelUtensilFactory()):
        bowl = utensil_factory.create_bowl()
        pan = utensil_factory.create_pan()
        bowl.bowl_maker()
        pan.pan_maker()

if __name__ == "__main__":
    main()



