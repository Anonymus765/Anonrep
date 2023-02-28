import datetime
class Student:
    name = ''
    birth = 2000
    group = 5
    bal = 10
    date = datetime.date.today().year

    def __init__(self, name='', birth=2000, group=5, bal=10, date = datetime.date.today().year):
        self.name = name
        self.birth = birth
        self.group = group
        self.bal = bal
        self.date = date
    def __str__(self):
        return \
            f'Name: {self.name}\n' \
            f'Health: {self.birth}\n' \
            f'Damage: {self.group}\n' \
            f'Defence: {self.bal}\n'
    def get_age(self):
        return self.date - self.birth