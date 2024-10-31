old = [1, 2, 3]
new = [ n+ 1 for n in old ]
print(new)


test = range(1,4)
print(list(test))

q = range(1,5)
new_q = [n *2 for n in list(q)]
print(new_q)

name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

cap_name = [name.upper() for name in name if len(name) > 5]

print(cap_name)


####each number in the new list should be squared
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

##### only take even number of the list
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
file_1 = [n for n in numbers if n % 2 == 0]
print(file_1)


with open('file1.txt' , 'r') as rf:
    content = rf.readlines()
    file_1 = []
    for n in content:
        file_1.append(int(n.strip()))

with open('file2.txt' , 'r') as rf:
    content = rf.readlines()
    file_2 = []
    for n in content:
        file_2.append(int(n.strip()))
print(file_1)
print(file_2)

result = [n for n in file_2 if n in file_1 ]
print(result)

###Dictionary Comprehension
import random

student_scores =  {student:random.randint(1,100) for student in name}
print(student_scores)

#created a new dict with only passed student
passed_students = {key:value for (key,value) in student_scores.items() if value > 50 }
print(passed_students)

"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the 
    given sentence and calculates the number of letters in each word."""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# created a list with lengths of each word in the senetence just for testing
test = sentence.split(' ')
print(test)
len_test = [len(n) for n in test]
print(len_test)

len_dict = {n:len(n) for n in sentence.split(' ')}

print(len_dict)

"""You are going to use Dictionary Comprehension to create a dictionary called weather_f 
that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f use this formula: 

(temp_c * 9/5) + 32 = temp_f

"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {key:(value * 9/5) +32  for (key,value) in weather_c.items()}

print(weather_f)