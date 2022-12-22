class Dinosaur:

    def __init__ (self, name):
        self.name = name
        self.attack_power = 100
        self.health = 400

    def attack (self, robot):
        robot.health -= self.attack_power
        pass