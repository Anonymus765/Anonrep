class Pomer(BaseException):
    def __init__(self, message=''):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message

class Person:
    name = ''
    health = 0
    mood = 0
    money = 0
    
    def __init__(self, name='', health=10, mood=10, money=55.9):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настроение: {self.mood}\n' \
            f' Деньги: {self.money}\n'
    def change_state(self, zdor, mod, mon):
        self.money += mon
        self.health += zdor
        self.mood += mod
        if self.money < 0:
            raise Pomer("Человек обонкротился")
        if self.health < 0:
            raise Pomer("Человек помер")
        if self.mood < 0:
            raise Pomer("У человека деппресия в ноль лет")
    def do(self, Act):
        self.money += Act.money
        self.health += Act.health
        self.mood += Act.mood
class Action:
    name = ''
    health = 0
    mood = 0
    money = 0