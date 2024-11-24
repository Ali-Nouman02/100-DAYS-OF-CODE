import requests
import datetime as dt
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

##  Use https://www.alphavantage.co/documentation/#daily

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_NAME}&interval=60min&apikey=4N5YRIU94CEN3VWC")
response.raise_for_status()
data = response.json()

now = dt.datetime.now()
today = str(now.today())
date_today = today.split(" ")[0]

#yesterday's date
date_object = dt.datetime.strptime(date_today, "%Y-%m-%d").date()
date_yesterday = str(date_object - dt.timedelta(days=1))
date_yesterday = date_yesterday + " " + "16:00:00"

#yesterdays's closing price
closing_price_yesterday = float(data["Time Series (60min)"][date_yesterday]["4. close"])

#day before yesterday date
date_day_before_yesterday = str(date_object - dt.timedelta(days=2))
date_day_before_yesterday = date_day_before_yesterday + " " + "16:00:00"
#day before yesterday closing price
closing_price_day_before_yesterday = float(data["Time Series (60min)"][date_day_before_yesterday]["4. close"])

#find the difference between the prices
difference = closing_price_day_before_yesterday - closing_price_yesterday
#calculate the percentage change in price
percentage_change = round((abs(difference)/closing_price_day_before_yesterday) * 100,2)
print(percentage_change)

send_email = False
if percentage_change > 5:
     send_email = True

#  https://newsapi.org/
# If the percentage change is greater than 5 then it will fetch the 3 news arctiles of that company
#https://newsapi.org/v2/everything?q=bitcoin&apiKey=4a91ea7913d74dff89eab6838dffbe09

if send_email == True:
    response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&language=en&apiKey=4a91ea7913d74dff89eab6838dffbe09")
    response.raise_for_status()
    data = response.json()
    articles = data["articles"][:3]

    #used list comprehension to make a list of deadlines and descriptions
    headlines = [(x["title"]) for x in articles]
    description = [x["description"] for x in articles]

    #checks if the difference was positive or negative
    if difference > 0:
        sign = "Down"
    elif difference < 0:
        sign = "Up"

    #- Send each article as a separate email
    my_email = "p39947641@gmail.com"
    password = "put your password here"
    for x in range(2):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="put recipient email here",
                msg=f"Subject:TSLA:{sign} {str(percentage_change)+"%"}\n\nHeadline:{headlines[x]}\nBrief:{description[x]}"
            )


print("code executed")

# format of the email
"""
TSLA: UP 2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: DOWN 5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

