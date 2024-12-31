Birthday Email Reminder:

This Python project sends personalized birthday wishes via email based on a provided CSV file containing the names, birthdates, and email addresses of recipients. The program checks if today's date matches any entries in the CSV file and sends a randomly chosen birthday greeting.

Features

1.Sends personalized birthday emails using predefined templates.
2Fetches email credentials securely from a .env file to ensure privacy.
3.Uses a CSV file to store birthdays, with columns for name, month, day, and email address.
4.Supports multiple birthday templates to randomize the email content.
5.The emails are sent through the Gmail SMTP server.

Requirements
  Before running the project, make sure to install the required libraries and configure the project settings:

Libraries
  pandas: For reading and processing the CSV file.
  smtplib: For sending emails via SMTP.
  dotenv: For loading email credentials securely from a .env file.
  random: For selecting a random birthday greeting template.

You can install the required libraries using:
  pip install pandas python-dotenv

Create a .env file at the project root and add your email credentials like so:
  
  EMAIL_USER=your_email@gmail.com
  EMAIL_PASS=your_password
  Note: Make sure that your email account allows access to less secure apps, or create an app-specific password if you're using two-factor authentication.

Files Structure
  main.py: Main Python script responsible for sending the birthday email.
  birthdays.csv: A CSV file containing the recipients' birthdays (columns: name, month, day, email).
  letter_templates/: Folder containing various birthday letter templates (letter_1.txt, letter_2.txt, letter_3.txt).
  .env: File containing the email credentials (EMAIL_USER, EMAIL_PASS).
  CSV Format
  The birthdays.csv file should have the following format:

  name,email,year,month,day
  mahesh,mahesh.xr@gmail.com,2005,12,31
  Templates:
   You can store various letter templates in the letter_templates/ directory. These templates should contain a placeholder ([NAME]) that will be replaced by the recipient's name in the email.

  Example (letter_1.txt):
  
  sql
  Copy code
  Dear [NAME],
  
  Happy Birthday! May your day be filled with joy, love, and happiness!
  
  Best Wishes,
  Your Name
