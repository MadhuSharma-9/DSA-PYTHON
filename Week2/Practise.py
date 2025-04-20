class Character:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
    def __attack__(self, other):
        print(self.name + " warrior attack dragon knight with his big sword")
        if self.strength > other.strength:
            print(self.name + " warrior wins")
        else:
            print(other.name + " dragon knight wins")
    
character = Character("Madhu", 100)
character2 = Character("dragon knight", 50)

print(character.__attack__(character2))
print(character2.__attack__(character))
