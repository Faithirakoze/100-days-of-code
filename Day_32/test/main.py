import datetime as dt
import random
import smtplib

MY_EMAIL = "faithirakoze51@gmail.com"
MY_PASSWORD = "koycqcstajdhjmpb"

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 6:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
        print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="faithirakoze51@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}."
        )




# date_of_birth = dt.datetime(year=2003, month=2, day=11)
# print(date_of_birth)