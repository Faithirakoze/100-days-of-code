##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas
import datetime as dt
import random
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = "faithirakoze51@gmail.com"
MY_PASSWORD = os.getenv("APP_PASSWORD")


data = pandas.read_csv('birthdays.csv')
# print(data)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict)

now = dt.datetime.now()
current_day = now.day
current_month = now.month
month_and_date = (current_month, current_day)

for key in birthday_dict:
    if key == month_and_date:
        birthday_person = birthday_dict[month_and_date]
        folder = "letter_templates"
        random_letter = random.choice(os.listdir(folder))
        file_path = os.path.join(folder, random_letter)

        with open(file_path, "r") as letter_file:
            data = letter_file.read()
            data = data.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{data}"
            )


