from Weapon import Weapon

class Robot:

    def __init__ (self, name):
        self.name = name
        self.health = 10
        self.active_weapon = "Weapon"

    def attack (self, dinosaur):
        pass