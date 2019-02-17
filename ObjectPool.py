
class ReusablePoolofLaptops:

    def __init__(self, size):
        self._reusables = [ReusableLaptop() for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()
    
    def release(self, reusable):
        self._reusables.append(reusable)
    

class ReusableLaptop:
    pass

def main():
    reusable_pool_of_laptops = ReusablePoolofLaptops(10)
    print(f"We currently have {len(reusable_pool_of_laptops._reusables)} laptops")
    print("Acquiring laptop for new employee")
    reusable = reusable_pool_of_laptops.acquire()
    print(f"We now have {len(reusable_pool_of_laptops._reusables)} laptops")
    print("Releasing the laptop since employee left the organization.")
    reusable_pool_of_laptops.release(reusable)
    print(f"We have {len(reusable_pool_of_laptops._reusables)} laptops once again!")

if __name__ == "__main__":
    main()
