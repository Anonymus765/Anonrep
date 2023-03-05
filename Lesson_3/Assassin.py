from Lesson_2.character import Character
from possibility import roll

class Assassin(Character):
    def __init__(self, name='Assassin', health=30, damage=5, defence=2):
        Character.__init__(self, name, health, damage, defence)
    def attack(self, enemy):
        if roll(1):
            enemy.take_damage(1000)
        else:
            enemy.take_damage(self.damage)
    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)