# Write your code below this line 👇
import math

import logo

# def paint_calc(height,width,cover):
#     print(round(((height*width)/cover),0))

# def paint_calc(height,width,cover):
#     num_cans=math.ceil(((height*width)/cover))
#     print('You need this amount of cans:'+ str(num_cans))

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
# paint_calc(3,9,5)


# def prime_checker(number):
#     if number%number==0 and number%1==0:
#         print(f'{number} is a prime number')
#     else:
#         print(f'{number} is not a prime number')
# prime_checker(4)
#first we need a range loop starting from 1 till the input number
#prime numbers can only cleanly divide bythemselves or 1
#this means prime counter should reach max 2
#if counter is greater than 2 then its not a prime number
# def prime_checker(number):
#     prime_counter = 0
#     for x in range(1, int(number)+1):
#         if number % x == 0:
#             prime_counter = prime_counter + 1
#
#     if prime_counter < 3:
#         print('prime number')
#     else:
#         print('not prime number')
#
# prime_checker(10)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import logo
print(logo.logo)
user_wants = True
while user_wants:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    # with index we can find out the position of the alphabet in the list
    # x = alphabet.index('a')
    # print(x)

    #logic
    # first we find out the position of the alphabet in the list
    # then i add shift number to that position
    # then i retrieve the alphabet in that list position

    # first we need to take the text and break into letters: DONE
    # then for each letter we need to find out the position
        #to do this we make a for loop
        # we find the position of each letter and save it
    # then to each position we will add the shift value
    # then we can print the encoded results

    def encrypt(text, shift):
        char_list  = list(text)
        result = []
        for x in range(0, len(char_list)):
            position = alphabet.index(char_list[x])
            get_position = position + int(shift)
            result.append(alphabet[get_position])
            encoded = ''.join(result)
        print (f'encoded message is: {encoded}')

    # encrypt('abc',1)

    #TODO: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    # first we need to take the text and break into letters
    # then for each letter we need to find out the position
        #to do this we make a for loop
        # we find the position of each letter and save it
    # then to each position we will minus the shift value
    # then we can print the encoded results
    def decrypt(text,shift):
        char_list = list(text)
        result = []
        for x in range(0, len(char_list)):
            position = alphabet.index(char_list[x])
            get_position = position - int(shift)
            result.append(alphabet[get_position])
            decoded = ''.join(result)
        print(f'decoded message is : {decoded}')
    # decrypt('bcd',1)

    # if direction == 'encode':
    #     encrypt(text, shift)
    # elif direction == 'decode':
    #     decrypt(text, shift)
    # else:
    #     print('Typo mistake')

    def ceaser(direction,text,shift):
        if direction == 'encode':
            char_list = list(text)
            result = []
            for x in range(0, len(char_list)):
                if char_list[x] in alphabet:
                    position = alphabet.index(char_list[x])
                    get_position = position + int(shift)
                    result.append(alphabet[get_position])
                    encoded = ''.join(result)
            print(f'encoded message is: {encoded}')
        elif direction == 'decode':
            char_list = list(text)
            result = []
            for x in range(0, len(char_list)):
                position = alphabet.index(char_list[x])
                get_position = position - int(shift)
                result.append(alphabet[get_position])
                decoded = ''.join(result)
            print(f'decoded message is : {decoded}')

    ceaser(direction,text,shift)
    user_wants = input('do you want the program again? yes or no\n')
    if user_wants == 'no':
        user_wants = False
