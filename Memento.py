import pickle

class Originator:
    def __init__(self):
        self._state = None
    
    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)
    
    def create_memento(self):
        return pickle.dumps(vars(self))

def main():
    originator = Originator()
    memento = originator.create_memento()
    originator._state = True
    originator.set_memento(memento)

if __name__ == "__main__":
    main()
