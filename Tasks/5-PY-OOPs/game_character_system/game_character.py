class GAME_CHARACTER:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and now has {self.health} health.")

    def display_status(self):
        status = "alive" if self.is_alive() else "dead"
        print(f"{self.name} | Status: {status} | Health: {self.health} | Level: {self.level}")

