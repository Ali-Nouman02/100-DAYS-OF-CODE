# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# #This is the scoring criteria:
# #Scores 91 - 100: Grade = "Outstanding"
# #Scores 81 - 90: Grade = "Exceeds Expectations"
# #Scores 71 - 80: Grade = "Acceptable"
# #Scores 70 or lower: Grade = "Fail"'
# student_grades = {}
# # TODO-2: Write your code below to add the grades to student_grades.👇
# #how do you add to a dictionary
# #student_grades['blah'] = "blah blah"
#
# student_grades =  {}
#
# for name in student_scores:
#     if student_scores[name] > 90 and student_scores[name] <= 100:
#         student_grades[name] = "Outstanding"
#     elif student_scores[name] > 80 and student_scores[name] <= 90:
#         student_grades[name] = "Exceeds Expectations"
#     elif student_scores[name] > 71 and student_scores[name] <= 80:
#         student_grades[name] = "Acceptable"
#     elif student_scores[name] <= 70:
#         student_grades[name] = "Fail"
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

# #Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris","lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
#
# #Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris","Lille","Dijon"],"total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits:": 5}
# }
# #Nesting Dictionary in a List
#
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ]

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string
# travel_log = []
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
#we need to add a new dictionary into travel log
# def add_new_country(country , visits, cities = []):
#     travel_log.append({
#     "country": country,
#     "visits": visits,
#     "cities":cities
#   })
#
# add_new_country("Pakistan" , 5, cities=['lahore','islamabad', 'Karachi'])
#
# # Do not change the code below 👇
# # add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")
#
# print(travel_log)
endofgame = True
bid_record = {}
while endofgame:
    name = input('What is your name\n')
    bid = int(input('What is your bid price?\n'))
    def function(name , bid):
        bid_record [name] = bid

    function(name, bid)
    next_user = input('is there any other users who wants to bid? yes or no? \n')
    if next_user == 'yes':
        endofgame = True
    elif next_user == 'no':
        endofgame = False

for keys in bid_record:
    print(keys + ' ' + str(bid_record[keys]))

current_record = 0
highest_bid = 0
for keys in bid_record:
    current_record = bid_record[keys]
    current_name = keys
    if current_record > highest_bid:
        highest_bid = current_record
        highest_name = current_name


print(f'{highest_name} has the highest bid of {highest_bid}')







