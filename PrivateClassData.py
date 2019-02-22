class DataClass:
    def __init__(self):
        self.value = None
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        if self.value is None:
            self.value = value

class MainClass:
    attribute = DataClass()

    def __init__(self, value):
        self.attribute = value
    
def main():
    m = MainClass(True)
    m.attribute = False

if __name__ == "__main__":
    main()