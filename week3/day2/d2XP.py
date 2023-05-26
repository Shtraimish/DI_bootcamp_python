#1 class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bengal_cat=Bengal('Vasiliy',3)
# chartreux_cat=Chartreux('Barsik',4)
# siamese_cat=Siamese('Felix',5)

# all_cats= [bengal_cat,chartreux_cat,siamese_cat]
# sara_pets=Pets(all_cats)
# sara_pets.walk()

2
class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        
    def bark (self):
        print(f'{self.name} is barking')
    def run_speed(self):
        return (self.weight/(self.age*10))
    
    def fight(self,other_dog):
        self_score=self.run_speed()*self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f'{self.name} won the fight!'
        elif self_score < other_score:
            return f'{other_dog.name} won the fight!'
        else:
            return "It's a tie!"

dog1 = Dog("Max", 3, 15)
dog2 = Dog("Bella", 5, 20)
dog3 = Dog("Charlie", 2, 12)

print(dog1.bark())
print(f"{dog1.name}'s running speed: {dog1.run_speed()}")

print(dog2.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")

print(dog3.bark())
print(f"{dog3.name}'s running speed: {dog3.run_speed()}")


