#1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        
# cat1=Cat('barsik',23)

# def catprint(Cat):
#     print('The oldest cat is',cat1.name,' and is',cat1.age, 'years old.')

# catprint(cat1)
#2
# class Dog:
#     def __init__(self,dog_name,dog_height) :
#         self.name=dog_name
#         self.height=dog_height
        
#         def bark(self):
#             print('{self.name}, goes woof')
#         def jump(self):
#             jump_height = self.height * 2
#             print('{self.name}, can jump for, {jump_height}*2, cm height')
# dog1= Dog('barbos',35)
# #dog1.jump()
# dog1.bark()
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
    
#     def bark(self):
#         print(f"{self.name} goes woof!")
    
#     def jump(self):
#         jump_height = self.height * 2
#         print(f"{self.name} jumps {jump_height} cm high!")

# dog1 = Dog("barbos", 35)
# dog2=Dog("Rex",50)
# dog3 = Dog("Teacup", 20)
# dog1.jump()
# print(dog2)
# dog2.bark()
# dog2.jump()
# if dog1.height > dog2.height and dog1.height > dog3.height:
#     print(f"The bigger dog is {dog1.name}.")
# elif dog2.height > dog1.height and dog2.height > dog3.height:
#     print(f"The bigger dog is {dog2.name}.")
# elif dog3.height > dog1.height and dog3.height > dog2.height:
#     print(f"The bigger dog is {dog3.name}.")
# else:
#     print("There are multiple dogs with the same size.")
#3
# class Song:
#     def __init__(self,lyrics):
#         self.lyrics=lyrics

#     def   sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line) 
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])  
# stairway.sing_me_a_song() 
#4
# class ZipImportError:
#     def __init__(self,zoo_name) :
#         self.name=zoo_name
#         self.animals=[]
#     def add_animal(self,new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#             print(f"{new_animal} has been added to the zoo!")
#         else:
#             print(f"{new_animal} is already in the zoo!")
#     def get_animals(self):
#         print(self.animals)
#     def sell_animal(self,animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#     def sort_animals(self):
#         sorted_animals = {}
#         for animal in self.animals:
#             first_letter = animal[0]
#             if first_letter in sorted_animals:
#                 sorted_animals[first_letter].append(animal)
#             else:
#                 sorted_animals[first_letter] = [animal]
        
#         sorted_animals = dict(sorted(sorted_animals.items()))
#         return sorted_animals
