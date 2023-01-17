##################### Hard Starting Project ######################
import pandas
import datetime as dt
from random import choice
import smtplib

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
d = dt.datetime.now()
today_tuple = (d.month, d.day)
if today_tuple in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    birthday_person = birthdays_dict[today_tuple]

    data1 = open("letter_templates/letter_1.txt", "r")
    data2 = open("letter_templates/letter_2.txt", "r")
    data3 = open("letter_templates/letter_3.txt", "r")
    choose = [data1.read().replace("[NAME]", birthday_person["name"]),
              data2.read().replace("[NAME]", birthday_person["name"]),
              data3.read().replace("[NAME]", birthday_person["name"])]
    print(choice(choose))
    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    mail = "haraham000@gmail.com"
    password = "zfhsucekpwfaiykx"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs=birthday_person["email"], msg=f"subject:Birthday wishes\n\n{choice(choose)}")








