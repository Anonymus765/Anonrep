from Lesson_2.character import Character
from possibility import roll

class Ninja(Character):
    def __init__(self, name='Ninja', health=20, damage=6, defence=1):
        Character.__init__(self, name, health, damage, defence)
    def take_damage(self, damage):
        if roll(25):
            print("Урон не був отриманий")
        else:
            self.health -= max(damage - self.defence, 0)