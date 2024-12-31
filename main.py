import os
import pandas as pd
import smtplib
import datetime as dt
from random import choice
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
PLACEHOLDER = '[NAME]'

# Fetch email credentials from .env file
USER_NAME = os.getenv('EMAIL_USER')
PASSWORD = os.getenv('EMAIL_PASS')

# Function to send an email
def send_email(message, email):
    """
    Sends an email to the specified address.
    :param message: The content of the email.
    :param email: Recipient's email address.
    """
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # Encrypt the connection
            connection.login(USER_NAME, PASSWORD)
            connection.sendmail(
                from_addr=USER_NAME,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )
            print(f"Email successfully sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to handle the birthday emails
def main():
    """
    Check if today matches any birthdays in the CSV file and send emails accordingly.
    """
    # Get today's date
    today = dt.datetime.now()
    today_month, today_day = today.month, today.day

    # Load the birthdays data from the CSV
    try:
        data = pd.read_csv('birthdays.csv')
    except FileNotFoundError:
        print("Error: 'birthdays.csv' file not found.")
        return

    # List of letter templates to choose from
    letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

    # Iterate through the birthdays dataset
    for _, row in data.iterrows():
        if row['month'] == today_month and row['day'] == today_day:
            name = row['name']
            email = row['email']

            # Choose a random template and personalize it
            try:
                template_path = f"letter_templates/{choice(letter_templates)}"
                with open(template_path) as template_file:
                    letter_content = template_file.read().replace(PLACEHOLDER, name)

                # Send the personalized email
                send_email(message=letter_content, email=email)

            except FileNotFoundError:
                print(f"Error: Letter template file '{template_path}' not found.")
                continue

if __name__ == "__main__":
    main()
