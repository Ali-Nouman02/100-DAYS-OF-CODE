import logo
import random
import game_data

def random_element():
    element = random.choice(game_data.data)
    return element
option_A = random_element()
option_B = random_element()
game_continue = True
current_score = 0
while game_continue:
    # print(logo.logo)

    print(f"Compare A:{option_A['name']}, a {option_A['description']}, from {option_A['country']}")
    print(logo.vs)
    print(print(f"Compare B:{option_B['name']}, a {option_B['description']}, from {option_B['country']}"))
    #make a input statement for user choice
    user_c = input("Who has more followers.Type 'A' or 'B': ").lower()
    def determine_answer():
        """this will check who has the most follower from both options"""
        if option_A['follower_count'] > option_B['follower_count']:
            return 'a'
        elif option_A['follower_count'] < option_B['follower_count']:
            return ('b')
    def correct_element():
        """this will give us the correct element"""
        if option_A['follower_count'] > option_B['follower_count']:
            return option_A
        elif option_A['follower_count'] < option_B['follower_count']:
            return option_B

    correct =  correct_element()
    answer_check = determine_answer()
    print(f"ans is:{answer_check}")
    print(f"user choice:{user_c}")

    if user_c == answer_check:
        print("you are right!")
        current_score += 1
        print(f"you current score is:{current_score}")
        option_A = correct
        # print(f"check{option_A}")
        option_B = random_element()
    elif user_c != answer_check:
        print("you are wrong!Game Over.")
        game_continue = False

