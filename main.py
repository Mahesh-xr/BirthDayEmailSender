##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import smtplib
import datetime as dt
from random import choice
USER_NAME = 'mahesh.rit.xr@gmail.com'
PASSWORD = "oian ldyx knxa uqvb"
PLACEHOLDER = '[NAME]'
email_to_send = ''
birthday_person = ''

def send_email(message, email):
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=USER_NAME, password=PASSWORD)
    connection.sendmail(
        from_addr=USER_NAME,
        to_addrs=email,
        msg=f"Subject:HBD\n\n{message}"
    )


letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
now = dt.datetime.now()
today_month = now.month
today_day = now.day
data = pandas.read_csv('birthdays.csv')


for (index, row) in data.iterrows():
    if row.day == today_day and row.month == today_month:
        birthday_person = row['name']
        email_to_send = row.email
        print(birthday_person)
        print(email_to_send)
        birthday_letter = choice(letters)
        with open(f"letter_templates/{birthday_letter}") as data_file:
            general_content = data_file.read()
            replaced_content = general_content.replace(PLACEHOLDER, birthday_person)
        send_email(message=replaced_content, email=email_to_send)


