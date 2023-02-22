import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')

if player_movie == 'r':
    player_movie = rock
elif player_movie == 'p':
    player_movie = paper
elif player_movie == 's':
    player_movie = scissors
else:
    raise SystemExit('Invalid Input. Try again ...')
computer_random_choice = random.randint(1, 3)
computer_movie = ''
if computer_random_choice == 1:
    computer_movie = rock
elif computer_random_choice == 2:
    computer_movie = paper
else:
    computer_movie = scissors

if (player_movie == rock and computer_movie == scissors) or \
        (player_movie == scissors and computer_movie == paper) or \
        (player_movie == paper and computer_movie == rock):
    print('Congrats, you win !')
elif (player_movie == rock and computer_movie == paper) or \
        (player_movie == scissors and computer_movie == rock) or \
        (player_movie == paper and computer_movie == scissors):
    print('Sorry, you lose !')
elif (player_movie == rock and computer_movie == rock) or \
        (player_movie == scissors and computer_movie == scissors) or \
        (player_movie == paper and computer_movie == paper):
    print('Draw !')
