from enum import Enum

class Kind(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"

    def __str__(self):
        return self.value

class Pet:
    # Constructor
    def __init__(self,
                name = "",
                breed = "",
                age = 0,
                greeting = "",
                mass = 0
                ):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass

    # Descructor
    def __del__(self):
        print(f"{self.name} has been destructed.")

    def __str__(self):
        return f"{self.name}, {self.breed}, Age: {self.age}, Greeting: {self.greeting}, Mass: {self.mass}"

    def isPolite(self):
        return True if self.greeting == "Hello" else False
    
class Home:
    # Constructor
    def __init__(self,
                 pets = []
                 ):
        self.pets = pets

    # Descructor
    def __del__(self):
        print("Home has been destructed.")

    def __str__(self):
        return f"Home with {len(self.pets)} pets."

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def get_pets(self):
        return self.pets

    def areFriends(self, pets):
        result = []
        for pet in pets:
            flag = False
            for home_pet in self.pets:
                if abs(pet.age - home_pet.age) <= 2:
                    flag = True
            result.append(flag)
        return result

def main():
    home = Home()
    pet1 = Pet(name="Buddy", breed=Kind.DOG, age=3, greeting="Hello", mass=30)
    pet2 = Pet(name="Whiskers", breed=Kind.CAT, age=5, greeting="Hi", mass=10)
    pet3 = Pet(name="Tweety", breed=Kind.BIRD, age=1, greeting="Hello", mass=0.1)

    home.add_pet(pet1)
    home.add_pet(pet2)

    print(f"{home}\nPets in the home:")
    for pet in home.get_pets():
        print(pet)

    friends_check = home.areFriends([pet1, pet2, pet3])
    print("\nAre the pets friends based on age proximity?")
    for i, pet in enumerate([pet1, pet2, pet3]):
        print(f"{pet.name}: {'Yes' if friends_check[i] else 'No'}")

    print() # Seperate the output for destructors' messages
main()