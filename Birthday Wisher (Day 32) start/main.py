import smtplib
import datetime as dt
import pandas as pd
import random


MY_EMAIL = "garimasaraswat85@gmail.com"
PASSWORD = "spikmleoznamelpq" #spik mleo znam elpq

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")


birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
""" eg :-  birthday_dict{

            (birth_month, birth_day) : name, email, month, daya 
            }
"""
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple] 
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])                

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}")


print(today_tuple)





