import random

#1 is rock, 2 is paper, and 3 is scissors
def game ():

  player_1 = input('Select rock, paper, or scissors \n')
  cpu = random.randint(1, 3)  
  player = 0
  computer = 0

  if player_1 == 'rock':
    if cpu == 1:
      print('You have tied\n')
    elif cpu == 2:
      print('The cpu wins!\n')
      computer += 1
    elif cpu == 3:
      print('Player 1 wins!\n')
      player += 1


  if player_1 == 'paper':
    if cpu == 1:
      print('Player 1 wins!\n')
      player += 1
    elif cpu == 2:
      print('You have tied\n')
    elif cpu == 3:
      print('The cpu wins!\n')
      computer += 1
  
  
  if player_1 == 'scissors':
    if cpu == 1:
      print('The cpu wins!\n')
      computer += 1
    elif cpu == 2:
      print('Player 1 wins!\n')
      player += 1
    elif cpu == 3:
      print('You have tied\n')
  return computer , player

while True:
  game()