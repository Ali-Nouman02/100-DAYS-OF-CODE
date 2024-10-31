import random
game_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = [] #need to get 2 random numbers from the list
computer = []#need to get 2 random numbers from the list
def deal_card():
    """this function will give a random element from cards list"""
    return random.choice(cards)

def calculate_score(list):
    if len(list) == 2 and 11 in list and 10 in list:  # this means its a blackjack!
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    result = sum(list)
    return result

for x in range (0,2):
    user.append(deal_card())
    computer.append(deal_card())

def third_card():
    game_continue = True
    while game_continue:

        score_user = calculate_score(user)
        score_computer = calculate_score(computer)
        print(f'these are the users cards:{user}')
        print(f'these are the computers cards:{computer}')

        print(f"this is the sum of user:{score_user}")
        print(f"this is the sum of computer:{score_computer}")
        #checks for a blackjack

        if score_user == 0 or score_computer == 0 or score_user > 21:
            game_continue = False

        another_card = input('would you like to pick another card?y or n: ')
        if another_card == 'y':
            user.append(deal_card())
            third_card()
        elif another_card == 'n':
            game_continue = False


third_card()
while calculate_score(computer) < 17 and calculate_score(computer) != 0:
    computer.append(deal_card())

def compare(score1, score2):
    if calculate_score(computer) == calculate_score(user):
        print('draw')
    elif calculate_score(user) == 0:
        print('user wins')
    elif calculate_score(computer)== 0:
        print('computer wins')
    elif calculate_score(user) > 21:
        print('user lost. computer wins')
    elif calculate_score(computer) > 21:
        print('computer lost. User wins')

compare(calculate_score(user),calculate_score(computer))
