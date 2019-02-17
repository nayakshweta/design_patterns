
class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
    
class MyClass(metaclass=Singleton):
    pass

def main():
    m1 = MyClass()
    m2 = MyClass()
    
    if id(m1) == id(m2):
        print("Singleton works, both variables contain the same instance!")
    else:
        print("Singleton failed, variables contain different instances.")

if __name__ == "__main__":
    main()

