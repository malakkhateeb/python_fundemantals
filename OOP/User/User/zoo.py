class Animal:
    def __init__(self, name, age=0, healthlevel=50, happinesslevel=50):
        self.name = name
        self.age = age
        self.healthlevel = healthlevel
        self.happinesslevel = happinesslevel

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.healthlevel}, Happiness: {self.happinesslevel}")
        return self

    def feed(self):
        self.happinesslevel += 10
        self.healthlevel += 10


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, age=50, healthlevel=60, happinesslevel=60)

    def feed(self):
        self.happinesslevel += 5
        self.healthlevel += 5

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, age=46, healthlevel=70, happinesslevel=70) 
    def feed(self):
        self.happinesslevel += 15
        self.healthlevel += 15

class Bird(Animal):
    def __init__(self, name, is_fly):
        self.is_fly=is_fly
        super().__init__(name, age=10, healthlevel=80, happinesslevel=80)
    def feed(self):
        self.happinesslevel += 11
        self.healthlevel += 11



class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def add_bird(self, name, is_fly):

        self.animals.append(Bird(name,is_fly))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bird("Malak",True)
zoo1.print_all_info()
