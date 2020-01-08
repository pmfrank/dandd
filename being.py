import math

class IllegalArgumentError(ValueError):
    pass

class Being():

    def __init__(self, *args, **kwargs):
        if len(kwargs) >= 9: # Attributes are Str, Dex, Con, Int, Wis, Cha, Speed, AC, HP
            self.attribute = dict()
            for key, value in kwargs.items():
                self.attribute[key] = value
            self.skills = dict()
            self.alignment = str()
            self.profbonus = int()
            self.initiative = int()
            self.languages = list()
            attributes = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
            self.modifier = dict()
            for attribute in attributes:
                self.modifier[attribute] = math.floor((self.attribute[attribute]-10) / 2)
        else:
            raise IllegalArgumentError

class Character(Being):

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.profession = str()
        self.race = str()
        self.profbonus = int()
        self.proficiencies = list()

    def __str__(self):
        return f'Name: {self.name} Strength: {self.attribute["strength"]} Dexterity: {self.attribute["dexterity"]} Constitution: {self.attribute["constitution"]} Intelligence: {self.attribute["intelligence"]} Wisdom: {self.attribute["wisdom"]} Charisma: {self.attribute["charisma"]} Armor Class: {self.attribute["ac"]} Hit Points: {self.attribute["hp"]}'

class Moster(Being):
    
    def __init__(self, creature, **kwargs):
        super().__init__(**kwargs)
        self.creature = creature
