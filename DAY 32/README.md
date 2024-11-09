# Birthday Wisher Project 🎉

This project is a Python-based automation tool that sends birthday wishes via email. It reads birthday data from a CSV file, checks for matches with today’s date, customizes a letter template, and sends a personalized email to the recipient.

## Features

1. **Automated Birthday Check**: Reads `birthdays.csv` to check if today matches any birthday.
2. **Letter Personalization**: If there’s a match, the script randomly selects a congratulatory letter template and replaces `[NAME]` with the recipient’s name.
3. **Email Sending**: Sends the customized message to the recipient via Gmail’s SMTP server.

## Setup

1. **Update `birthdays.csv`**:
   - Add names, emails, and birthday dates in the following format:

     | name  | email             | month | day |
     |-------|--------------------|-------|-----|
     | John  | john@example.com   | 5     | 17  |
     | Alice | alice@example.com  | 8     | 23  |

2. **Configure Email Credentials**:
   - Update the `sender_email` and `password` fields in the script with your Gmail account credentials.

## Usage

1. **Add Letter Templates**:
   - Place your birthday letter templates in the `letter_templates` directory (e.g., `letter_1.txt`, `letter_2.txt`, etc.).

2. **Run the Script**:
   - Execute the script to automatically send birthday wishes:
     ```bash
     python birthday_wisher.py
     ```


