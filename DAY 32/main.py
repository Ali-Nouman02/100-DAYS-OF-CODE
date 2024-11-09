##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
import os

# 1. Update the birthdays.csv
#done

# 2. Check if today matches a birthday in the birthdays.csv
#convert the csv into a dataframe
df = pd.read_csv("birthdays.csv")
#loop through the df to see if there is a person who has a birthday today
now = dt.datetime.now()
month = now.month
day = now.day

bd_person = ""
bd_person_email = ""
def check_birthday():
    for i,row in df.iterrows():
        if row["month"] == month and row["day"] == day:
            bd_person = row["name"]
            bd_person_email = row["email"]

            return True,bd_person,bd_person_email
        else:
            return False
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

#getting the values from the function
check,bd_person, bd_person_email = check_birthday()

#it will only run if step one was true
if check == True:
    directory = "C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 32\\birthday-wisher-extrahard-start\\letter_templates"
    letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]
    random_letter = random.choice(letter_list)
    filepath = directory+"\\"+random_letter

    #loop through the directory
    for file in os.listdir(directory):
        if file == random_letter:

            #read the file and save the contents in a variable
            with open(filepath, 'r') as file:
                content = file.read()

            #replace the [NAME] with the actual person who has the birthday
            email_content = content.replace('[NAME]', bd_person)

# 4. Send the letter generated in step 3 to that person's email address.
sender_email = "p39947641@gmail.com"
password = "enter the password of the sender here"

if email_content:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs="enter the email of the recipient here",
            msg=f"Subject:Happy Birthday!!!\n\n{email_content}"
        )



