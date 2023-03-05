from Lesson_2.character import Character

class Samurai(Character):
    damapp = 0
    def __init__(self, name='Samurai', health=20, damage=7, defence=2):
        Character.__init__(self, name, health, damage, defence)
    def attack(self, enemy, damapp):
        if damapp <= 50:
            damapp ++ 10
        else:
            damapp = 0
        enemy.take_damage(self.damage + (self.damage / 100 * damapp))
    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)