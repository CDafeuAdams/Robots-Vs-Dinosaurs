from Dinosaur import Dinosaur
from Robot import Robot

class Battlefield:

    def __init__ (self):
        self.dinosaur = Dinosaur("T-Rex", 400)
        self.robot = Robot("Terminator", 400 )
        pass
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print("Welcome to the Game")
        pass

    def battle_phase(self):
        while self.dinosaur.health and self.robot.health > 0:
        self.dinosaur.attack(self.robot)

        pass

    def display_winner(self):
        pass
