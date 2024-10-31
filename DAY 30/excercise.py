# fruits = ["Apple", "Pear", "Orange"]
#"
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
#
#
# """Use what you've learnt about exception handling to prevent the program from crashing.
# If the user enters something that is out of range just print a default output of
# "Fruit pie". ""
#
# try:
#     make_pie(4)
# except IndexError:
#     print("Fruit pie")
# else:
#     make_pie(4)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
#
# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         total_likes = total_likes + post['Likes']
#
#     return total_likes
#
# try:
#     count_likes(facebook_posts)
# except KeyError:
#     print("this key does not exist")
# else:
#     count_likes(facebook_posts)
