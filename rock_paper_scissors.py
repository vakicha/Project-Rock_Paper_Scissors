import random


def question_check(questions):
    if questions == 'no':
        if computer_score > player_score:
            print('Now you lose, but next time you will win!')
        elif computer_score == player_score:
            print('You are draw!\nGood luck next time!')
        else:
            print('You win the game, MONSTER!')
        exit(0)
    else:
        print('Wrong choice! Good bye!')
        exit(0)


rock = 'rock'
paper = 'paper'
scissors = 'scissors'
computer_score = 0
player_score = 0
player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')
while player_movie != 'exit':

    # player definitions
    if player_movie == 'r':
        player_movie = rock
    elif player_movie == 'p':
        player_movie = paper
    elif player_movie == 's':
        player_movie = scissors
    else:
        print('Invalid choice!\nTry again')
        player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')
        continue

    # computer logic
    computer_random_choice = random.randint(1, 3)
    computer_movie = ''
    if computer_random_choice == 1:
        computer_movie = rock
    elif computer_random_choice == 2:
        computer_movie = paper
    else:
        computer_movie = scissors

    # game potentialities
    if (player_movie == rock and computer_movie == scissors) or \
            (player_movie == scissors and computer_movie == paper) or \
            (player_movie == paper and computer_movie == rock):
        player_score += 1
        print('Congrats, you win!')
        print(f'The result of the game is: YOU->{player_score:2d}, CPU->{computer_score:2d}')
        question = input('Do you want to continue?:')
        if question == 'yes':
            player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')
            continue
        else:
            question_check(question)
    elif (player_movie == rock and computer_movie == paper) or \
            (player_movie == scissors and computer_movie == rock) or \
            (player_movie == paper and computer_movie == scissors):
        computer_score += 1
        print('Sorry, you lose!')
        print(f'The result of the game is: YOU->{player_score:2d}, CPU->{computer_score:2d}')
        question = input('Do you want to continue?:')
        if question == 'yes':
            player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')
            continue
        else:
            question_check(question)
    elif (player_movie == rock and computer_movie == rock) or \
            (player_movie == scissors and computer_movie == scissors) or \
            (player_movie == paper and computer_movie == paper):
        computer_score += 1
        player_score += 1
        print('Draw!')
        print(f'The result of the game is: YOU->{player_score:2d}, CPU->{computer_score:2d}')
        question = input('Do you want to continue?:')
        if question == 'yes':
            player_movie = input('Choice [r]ock, [p]aper, [s]cissors: ')
            continue
        else:
            question_check(question)
if player_movie == 'exit':
    print('Thank you for the game!\nSee you next time!')
