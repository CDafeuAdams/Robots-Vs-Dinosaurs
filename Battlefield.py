from Dinosaur import Dinosaur

class Battlefield:

    def __init__ (self):
        self.dinosaur = Dinosaur("T-Rex", 20)
        pass
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
