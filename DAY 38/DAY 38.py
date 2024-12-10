import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")
GENDER = "male"
WEIGHT = 75
HEIGHT = 188
AGE = 22

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_text = input("Tell me what excercise you did")

headers  = {
    "x-app-id" : API_ID,
    "x-app-key": API_KEY,
}
print(headers)

params = {
    "query" : excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(excercise_endpoint, json = params,  headers = headers)
result = response.json()
print(result)

time_now = dt.datetime.now().time().strftime("%X")
date_today = dt.datetime.now().date().strftime('%d/%m/%Y')

####### sheetly section of the code ######

sheety_endpoint = os.getenv("sheety_endpoint")

for excercise in result["exercises"]:
    new_row_data = {
        "workout": {  # Root property as required by Sheety
            "date": date_today,
            "time": time_now,
            "exercise": excercise["name"].title(),
            "duration" : excercise["duration_min"],
            "calories" : excercise["nf_calories"]
        }
    }

USERNAME = os.getenv("USERNAME_sheety")
PASSWORD = os.getenv("PASSWORD")


response = requests.post(sheety_endpoint, json=new_row_data,
    auth=(USERNAME,PASSWORD,))
print(response.text)



