from Person import Person
from Person import Pomer
from Person import Action
import random

chel = Person(name = "Andrei", health = 10, mood = 9, money = 100)



go_to_park = Action(name = "Парк", money = 0, mood = 15, health = 3)

while True:
    try:
        chel.change_state(
            zdor = random.randint(50, 200),
            mod = random.randint(-20, -10),
            mon = random.randint(-10, -5)
        )
    except Pomer:
        print('Один из ресурсов закончился')
        raise ResourceEnd
    break
