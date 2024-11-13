import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

# Email credentials from environment variables
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

def document_initialised(browser):
    return browser.execute_script("alert('Alert via selenium')")

options = Options()
options.add_argument("--disable-extensions")

service = Service(r"yourpath\to\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
browser.get("https://shotgun.live/fr/login?redirect=%2F%3Futm_source%3Dgoogle")

# Account credentials from environment variables
username_account_Shotgun = os.getenv("SHOTGUN_USERNAME")
password_account_Shotgun = os.getenv("SHOTGUN_PASSWORD")

# Ensure account credentials are set
if not username_account_Shotgun or not password_account_Shotgun:
    raise ValueError("Shotgun account credentials are not set in environment variables")


browser.maximize_window()

WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.NAME, "email"))
username = browser.find_element (By.NAME,"email") 
username.send_keys (username_account_Shotgun) 

WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.NAME, "password"))
password = browser.find_element (By.NAME,"password") 
browser.implicitly_wait(10)
password.send_keys (password_account_Shotgun) 

ActionChains(browser).move_to_element(password).send_keys (Keys.RETURN).perform() 

browser.get("Link to the event you are targeting")

# Find all elements with the specified class name
elements = browser.find_elements(By.CSS_SELECTOR, ".light\\:drop-shadow.flex.flex-col.gap-6.rounded.border-2.p-6.md\\:flex-row.md\\:items-center.cursor-pointer.light.border-transparent")

# Check if there is more than one element
if len(elements) > 1:
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Ticket available"

    # Email body
    body = "This is an email sent from Python. A ticket is available for ... event!"
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, "your key")

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Close the SMTP server
    server.quit()
else:
    print("No ticket available")

browser.quit()



