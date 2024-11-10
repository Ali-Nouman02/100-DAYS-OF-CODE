import requests
import datetime as dt
import smtplib
import time

MY_LAT = 50.553890
MY_LONG = 9.674310
sender_email = "enter the sender email address here"
password = "enter the password here"

def check_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    """Check if the ISS is within 5 degrees of both latitude and longitude of the given position"""
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def dark_check():
    """checks if its currently dark"""
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now()
    current_hour = now.hour

    if current_hour >= sunset:
        return True
    else:
        return False

def iss_location_notifier():
    if check_iss_pos() and dark_check():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs="enter recipient email here",
                msg="Subject:International Space Station!\n\nLook up! The international Space Station just passed above you"
            )

while True:
    time.sleep(60)
    print(f"code executed. Time {dt.datetime.now()}")
    iss_location_notifier()


