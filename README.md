# Ticket Availability Detector and Email Notifier

This project automates the process of checking ticket availability on Shotgun and sends an email notification when tickets are available.
Handle the situation where there is still one category of tickets available but some categories at a lower price reappear from time to time.

## Features

- Logs into Shotgun using provided credentials
- Checks for ticket availability on a specified event page
- Sends an email notification if tickets are available

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- Shotgun account
- Gmail account (for the sender)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/helloelora/Ticket-available.git
    cd Ticket-available
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3.  Create a `.env` file in the root directory of the project with the following content:
    ```env
    SHOTGUN_USERNAME=your_shotgun_username
    SHOTGUN_PASSWORD=your_shotgun_password
    SENDER_EMAIL=your_email@example.com
    RECEIVER_EMAIL=receiver_email@example.com
    KEY_EMAIL=your Application password created via Gmail
    ```

4. Download ChromeDriver and place it in a known location. Update the path in the script:
    ```python
    service = Service(r"yourpath\to\chromedriver.exe")
    ```

## Usage

Run the script:
```sh
python Detect&Mail.py
