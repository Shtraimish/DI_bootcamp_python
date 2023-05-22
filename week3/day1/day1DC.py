class Farm:
    def __init__(self,farm_mane) :
        self.farm_name=farm_mane
        self.animals={}
    
    def add_animal(self,animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] =+ count
        else:
            self.animals[animal_type] = count
    def get_info(self):
        info=f"{self.farm_name}s farm\n"
        for animal, count in self.animals.items():
            info+= f"{animal}:{count}\n"
        info += "E-I-E-I-0!"
        return info     
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
        
    def get_short_info(self):
        animal_types=self.get_animal_types()
        animal_list=", ".join(animal_types)
        return f"{self.farm_name}s farm has{animal_list}"

macdonald = Farm("McDonald")
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())