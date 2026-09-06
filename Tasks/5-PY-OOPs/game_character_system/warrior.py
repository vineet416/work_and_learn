from game_character import GAME_CHARACTER

class WARRIOR(GAME_CHARACTER):
    def __init__(self, name, health, level, sword_power):
        super().__init__(name, health, level)
        self.sword_power = sword_power


    def sword_attack(self, target):
        print(f"{self.name} attacks {target.name} with a sword!")
        target.take_damage(self.sword_power)


    