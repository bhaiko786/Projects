import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import time
from datetime import datetime
import sys

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "Sandeepjain1993ok@gmail.com"
# Use App Password instead of regular password
APP_PASSWORD = "#Bjp4Mp@07"  # Generate this from Google Account settings
DAILY_LIMIT = 500
DELAY_BETWEEN_EMAILS = 2  # seconds between emails to avoid rate limiting

# CSV file configuration
CSV_FILE = "email_list.csv"

# Logging configuration
logging.basicConfig(
    filename=f"email_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmailSender:
    def __init__(self):
        self.server = None
        self.connect_attempts = 0
        self.max_attempts = 3

    def connect_to_smtp(self):
        """Establish SMTP connection with retry mechanism"""
        while self.connect_attempts < self.max_attempts:
            try:
                self.server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                self.server.starttls()
                self.server.login(FROM_EMAIL, APP_PASSWORD)
                logging.info("Successfully connected to SMTP server")
                return True
            except Exception as e:
                self.connect_attempts += 1
                logging.error(f"SMTP connection attempt {self.connect_attempts} failed: {str(e)}")
                if self.server:
                    self.server.quit()
                time.sleep(5)  # Wait before retrying
        return False

    def send_email(self, to_email, subject, body):
        """Send individual email with error handling"""
        if not self.server and not self.connect_to_smtp():
            logging.error("Failed to establish SMTP connection")
            return False

        try:
            # Create message container
            msg = MIMEMultipart()
            msg["From"] = FROM_EMAIL
            msg["To"] = to_email
            msg["Subject"] = subject

            # Add custom headers to avoid spam filters
            msg["Reply-To"] = FROM_EMAIL
            msg["X-Priority"] = "1"  # High priority

            # Attach text body
            msg.attach(MIMEText(body, "html"))  # Changed to HTML format for better formatting

            # Send email
            text = msg.as_string()
            self.server.sendmail(FROM_EMAIL, to_email, text)
            logging.info(f"Email sent successfully to {to_email}")
            return True

        except smtplib.SMTPServerDisconnected:
            logging.error("SMTP Server disconnected. Attempting to reconnect...")
            self.server = None
            return self.send_email(to_email, subject, body)  # Retry once
        except Exception as e:
            logging.error(f"Email failed to send to {to_email}: {str(e)}")
            return False

    def read_csv_and_send_emails(self):
        """Process CSV file and send emails"""
        sent_count = 0
        failed_emails = []

        try:
            with open(CSV_FILE, "r", encoding='utf-8') as file:
                reader = csv.DictReader(file)
                total_rows = sum(1 for row in csv.DictReader(open(CSV_FILE)))
                file.seek(0)  # Reset file pointer
                next(reader)  # Skip header row

                for row in reader:
                    try:
                        name = row["Name"].strip()
                        email = row["Email"].strip()
                        message = row["Message"].strip()
                        
                        # Basic email validation
                        if not '@' in email or not '.' in email:
                            logging.warning(f"Invalid email format: {email}")
                            failed_emails.append((email, "Invalid email format"))
                            continue

                        subject = f"Custom Email for {name}"
                        
                        # Create HTML message
                        html_message = f"""
                        <html>
                            <body>
                                <p>Dear {name},</p>
                                <div>{message}</div>
                                <p>Best regards,<br>Your Name</p>
                            </body>
                        </html>
                        """

                        if self.send_email(email, subject, html_message):
                            sent_count += 1
                            print(f"Progress: {sent_count}/{total_rows} - Email sent to {email}")
                        else:
                            failed_emails.append((email, "Sending failed"))
                            print(f"Failed to send to {email}")

                        # Respect daily limit
                        if sent_count >= DAILY_LIMIT:
                            print("Daily email limit reached. Stopping.")
                            break

                        # Add delay between emails
                        time.sleep(DELAY_BETWEEN_EMAILS)

                    except KeyError as e:
                        logging.error(f"Missing required column in CSV: {str(e)}")
                        print(f"Error: CSV file is missing required column: {str(e)}")
                        break

        except FileNotFoundError:
            logging.error(f"CSV file not found: {CSV_FILE}")
            print(f"Error: Could not find CSV file: {CSV_FILE}")
            return
        except Exception as e:
            logging.error(f"Error processing CSV file: {str(e)}")
            print(f"Error processing CSV file: {str(e)}")
            return
        finally:
            if self.server:
                self.server.quit()

        # Print summary
        print("\nEmail Sending Summary:")
        print(f"Total emails sent successfully: {sent_count}")
        print(f"Total failed emails: {len(failed_emails)}")
        if failed_emails:
            print("\nFailed email addresses:")
            for email, reason in failed_emails:
                print(f"- {email}: {reason}")

if __name__ == "__main__":
    sender = EmailSender()
    sender.read_csv_and_send_emails()