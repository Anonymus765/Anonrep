from Lesson_2.character import Character
from berserk import Berserk
from tank import Tank

player1 = Tank(name='Vasya', damage=10, defence=3)
player2 = Berserk(name='Petya', damage=10)

print(f' - Player 1 - \n{player1}')
print(f' - Player 2 - \n{player2}')

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    # player2.health -= max(player1.damage, 0)
    print('Player 1 attacted Player 2')
    player2.attack(player1)
    print('Player 2 attacted Player 1')

    print(f' - Player 1 - \n{player1}')
    print(f' - Player 2 - \n{player2}')
    print('\n\n')