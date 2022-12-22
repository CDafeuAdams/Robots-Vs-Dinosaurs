from Weapon import Weapon

class Robot:

    def __init__ (self, name):
        self.name = name
        self.health = 400
        self.active_weapon = Weapon("shotgun", 100)

    def attack (self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        pass