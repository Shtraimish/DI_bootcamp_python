class Character:
    def __init__(self,name) :
        self.name=name
        self.life=20
        self.attack=10
        
    def basic_attack(self,other_charachter):
        other_charachter.life -=self.attack
        print(f"{self.name} attacked{other_charachter.name}.{other_charachter.name}'s life points decreased to {other_charachter.life}.")
        
character1 = Character("Character 1")
character2 = Character("Character 2")

print(f"{character1.name}'s life points:", character1.life)
print(f"{character2.name}'s life points:", character2.life)

character1.basic_attack(character2)
character2.basic_attack(character1)

print(f"{character1.name}'s life points:", character1.life)
print(f"{character2.name}'s life points:", character2.life)


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("hello there. here am I and all the wolfs")
    
    def meditate(self):
        self.life+=10
        self.attack-=2
        print(f"{self.name} meditated. Life increased by 10 and attack decreased by 2.")
    
    def animal_help(self):
        self.attack+=5
        print(f"{self.name} called upon animal spirits. Attack increased by 5.")
    
    def fight(self,other_character):
        damage = int(0.75 * self.life + 0.75 * self.attack)
        other_character.life -= damage
        print(f"{self.name} fought against {other_character.name}. {other_character.name}'s life points decreased by {damage}.")
        
        
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print("A fearless Warrior has joined the battle!")

    def brawl(self, other_character):
        damage = 2 * self.attack
        self.life += int(0.5 * self.attack)
        other_character.life -= damage
        print(f"{self.name} engaged in a brawl with {other_character.name}. {other_character.name}'s life points decreased by {damage} and {self.name}'s life points increased.")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trained hard. Attack and life points increased by 2.")

    def roar(self, other_character):
        other_character.attack -= 3
        print(f"{self.name} let out a powerful roar. {other_character.name}'s attack decreased by 3.")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("A mysterious Mage has arrived!")

    def curse(self, other_character):
        other_character.attack -= 2
        print(f"{self.name} cast a curse on {other_character.name}. {other_character.name}'s attack decreased by 2.")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summoned magical energy. Attack increased by 3.")

    def cast_spell(self, other_character):
        damage = int(self.attack / 5)
        other_character.life -= damage
        print(f"{self.name} cast a spell on {other_character.name}. {other_character.name}'s life points decreased by {damage}.")


# Example usage
druid = Druid("Druid")
warrior = Warrior("Warrior")
mage = Mage("Mage")

druid.meditate()
warrior.brawl(druid)
mage.curse(warrior)

print(f"{druid.name}'s life points:", druid.life)
print(f"{warrior.name}'s life points:", warrior.life)
print(f"{mage.name}'s life points:", mage.life)