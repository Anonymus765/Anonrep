from Lesson_2.character import Character
from possibility import roll

class Ninja(Character):
    def __init__(self, name='Ninja', health=30, damage=5, defence=2):
        Character.__init__(self, name, health, damage, defence)
    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)
    def attack(self, enemy):
        enemy.take_damage(self.damage)
        self.health += max(self.damage / 100 * 10)
