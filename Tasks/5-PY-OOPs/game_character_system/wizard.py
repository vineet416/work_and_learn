from game_character import GAME_CHARACTER


class WIZARD(GAME_CHARACTER):
    def __init__(self, name, health, level, magic_power):
        super().__init__(name, health, level)
        self.magic_power = magic_power

    def magic_attack(self, target):
        print(f"{self.name} attacks {target.name} with magic!")
        target.take_damage(self.magic_power)