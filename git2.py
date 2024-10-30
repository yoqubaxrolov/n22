class Car:
    def __init__(self, name, cost):
        self.name = name 
        self.cost = cost
        self.owner = False

        def str(self):
            return "car class"


name = input("ismingizni kiriting ")
car = Car("BMW", 120000000)
car.owner = name
print(f"maashina nomi: {car.name}, narxi: {car.cost}, yangi mashina egasining ismi: {car.owner}")