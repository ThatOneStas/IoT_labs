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

    # Destructor
    def __del__(self):
        print(f"{self.name} has been destructed.")

    def __str__(self):
        return f"{self.name}, {self.breed}, Age: {self.age}, Greeting: {self.greeting}, Mass: {self.mass}"

    def is_polite(self):
        return True if "Hello" in self.greeting else False
    
class Home:
    # Constructor
    def __init__(self,
                 pets = None
                 ):
        if pets is None:
            self.pets = []    
        else:
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

    def sort_by_age(self, mode="asc"):
        n = len(self.pets)
        is_asc = (mode == "asc")
    
        for i in range(n):
            for j in range(0, n - i - 1):
                if (is_asc and self.pets[j].age > self.pets[j + 1].age) or \
                    (not is_asc and self.pets[j].age < self.pets[j + 1].age):
                    self.pets[j], self.pets[j + 1] = self.pets[j + 1], self.pets[j]


    def are_friends(self, pets):
        result = []
        for pet in pets:
            flag = False
            for home_pet in self.pets:
                if abs(pet.age - home_pet.age) < 2:
                    flag = True
            result.append(flag)
        return result

def main():
    home = Home()
    pet1 = Pet(name="Buddy", breed=Kind.DOG, age=3, greeting="Hello", mass=30)
    pet2 = Pet(name="Whiskers", breed=Kind.CAT, age=5, greeting="Hi", mass=10)
    pet3 = Pet(name="Tweety", breed=Kind.BIRD, age=2, greeting="Hello", mass=0.1)
    pet4 = Pet(name="Mikey", breed=Kind.DOG, age=10, greeting="Hello", mass=20)

    home.add_pet(pet1)
    home.add_pet(pet2)

    # show pets in home and check if they are polite
    print(f"{home}\nPets in the home:")
    for pet in home.get_pets():
        print(f"{pet} (is polite - {pet.is_polite()})")

    # check if pets of the list could be friends with home's pets
    pet_list = [pet1, pet2, pet3, pet4]
    friends_check = home.are_friends(pet_list)
    print("\nAre the pets friends based on age proximity?")
    for i, pet in enumerate(pet_list):
        print(f"{pet.name}: {'Yes' if friends_check[i] else 'No'}")

    home.add_pet(pet3)
    home.add_pet(pet4)

    # check home's age-sorting
    home_pets = home.get_pets()
    print("\nHome's pet list before being sorted:")
    for pet in home_pets:
        print(pet)

    home.sort_by_age()

    print("\nHome's pet list after being sorted:")
    for pet in home_pets:
        print(pet)

    print() # Separate the output for destructors' messages
main()