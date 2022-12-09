from Dinosaur import Dinosaur
from Robot import Robot

class Battlefield:

    def __init__ (self):
        self.dinosaur = Dinosaur("T-Rex", 400)
        self.robot = Robot("Terminator", 400)
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
            print(f"\nLet the Games Begin! {self.dinosaur.health and self.robot.health}")
        if self.dinosaur.attack_power == 100:
            self.robot.health -= 100
        if self.robot.active_weapon == 100:
            self.dinosaur.health -= 100
        if self.dinosaur.attack_power == 200:
            self.robot.health -= 200

        pass

    def display_winner(self):
        if self.dinosaur.health > 100:
            print(f"You are the Winner of the Battlefield!")
        elif self.robot.health <= 100:
            print(f"You are the winner of the Battlefield!")
        pass
