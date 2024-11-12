import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.keys import Keys


# Configuration
CSV_FILE = 'contacts.csv'
DELAY_BETWEEN_MESSAGES = 300  # 5 minutes in seconds
WHATSAPP_WEB_URL = 'https://web.whatsapp.com'


# Function to initialize the driver and open WhatsApp Web
def initialize_driver():
    """Initialize Safari driver"""
    options = Options()
    options.add_argument('--user-data-dir=./User_Data')  # Persistent login


    driver = webdriver.Safari(options=options)
    driver.get(WHATSAPP_WEB_URL)
    input("Please scan the QR code on WhatsApp Web and press Enter to continue...")
    return driver


# Function to send a message to a specific contact
def send_message(driver, phone, message):
    """Send a message to a contact via WhatsApp Web"""
    try:
        driver.get(f'{WHATSAPP_WEB_URL}/send?phone={phone}&text={message}')
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]'))
        )
        message_box.click()
        time.sleep(1)  # Small delay to ensure focus
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        return True
    except Exception as e:
        print(f"Failed to send message to {phone}: {e}")
        return False


# Main function to send bulk messages
def send_bulk_messages(filename):
    """Send bulk messages from CSV file"""
    driver = initialize_driver()
    count = 0

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            phone = row['Phone']
            message = row['Message']
            personalized_message = f"Hello {name}, {message}"

            count += 1
            if send_message(driver, phone, personalized_message):
                print(f"Message #{count} sent successfully to {name} at {phone}")
            else:
                print(f"Message #{count} failed to send to {name} at {phone}")

            print(f"Waiting {DELAY_BETWEEN_MESSAGES / 60} minutes before sending the next message...")
            time.sleep(DELAY_BETWEEN_MESSAGES)

    driver.quit()


if __name__ == '__main__':
    send_bulk_messages(CSV_FILE)