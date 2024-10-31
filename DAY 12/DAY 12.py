import random
def number_guess():
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number from 1 to 100')
    difficulty_level = input("chose a difficulty.Type 'easy' or 'hard':  ").lower()
    #define the diffculty level
    if difficulty_level == 'easy':
        lives = 10
        print('You have 10 lives remaining')
    elif difficulty_level =='hard':
        lives = 5
        print('You have 5 lives remaining')
    #pick a random integer from 1 to 100
    RANDOM_INTEGER = random.randint(1,100)
    print(f'the answer is {RANDOM_INTEGER}')
    # user_guess = input("Make a guess: ")
    def get_user_guess():
        guess = int(input("Make a guess: "))
        return guess
    user_wins = False
    while lives > 0 and not user_wins:
        guess = get_user_guess()
        if guess < RANDOM_INTEGER:
            lives -= 1
            print(f'remaining lives: {lives}')
            print('to low')
            print(f"you have {lives} remaining")
        elif guess > RANDOM_INTEGER:
            lives -= 1
            print(f'remaining lives: {lives}')
            print('to high')
            print(f"you have {lives} remaining")
        elif guess == RANDOM_INTEGER:
            user_wins = True
            print(f'you got it!. The answer is {RANDOM_INTEGER}')

        if lives == 0:
            print('no more lives remaining. You lose')
            replay = input("type 'again' to play again. type 'exit' to exit.: ")
            if replay == 'again':
                number_guess()
            else:
                print("the end")
        elif user_wins:
            print('you won')
            replay = input("type 'again' to play again. type 'exit' to exit.: ")
            if replay == 'again':
                number_guess()
            else:
                print("the end")
number_guess()