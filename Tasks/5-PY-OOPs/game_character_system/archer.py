from game_character import GAME_CHARACTER


class ARCHER(GAME_CHARACTER):
    def __init__(self, name, health, level, arrow_power):
        super().__init__(name, health, level)
        self.arrow_power = arrow_power

    def arrow_attack(self, target):
        print(f"{self.name} attacks {target.name} with an arrow!")
        target.take_damage(self.arrow_power)