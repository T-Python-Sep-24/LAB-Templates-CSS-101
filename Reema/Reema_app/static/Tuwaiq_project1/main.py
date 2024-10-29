import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Function to send reminder email
def send_reminder_email(recipient, subject, body):
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish connection and send email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error: {e}")

# Main function to handle reminders
def main():
    # List of recipients
    recipients = ['user1@example.com', 'user2@example.com']
    
    # Dictionary for reminders
    reminders = {
        'user1@example.com': 'Meeting at 3 PM',
        'user2@example.com': 'Project deadline tomorrow'
    }
    
    # Current time
    current_time = datetime.datetime.now()
    
    # Loop through recipients
    for recipient in recipients:
        # Check if the recipient has a reminder
        if recipient in reminders:
            subject = "Reminder"
            body = reminders[recipient]
            send_reminder_email(recipient, subject, body)
    
    # While loop for user input
    while True:
        user_input = input("Do you want to add another reminder? (yes/no): ")
        if user_input.lower() == 'yes':
            email = input("Enter email: ")
            reminder = input("Enter reminder: ")
            reminders[email] = reminder
            print(f"Reminder added for {email}.")
        elif user_input.lower() == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Run the main function
if __name__ == "__main__":
    main()