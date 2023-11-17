---
# BASIC GUI for mailgun api

This Email Management System is a PyQt5-based desktop application that interfaces with the Mailgun API to send emails and create routing rules. It offers a user-friendly graphical interface for entering email details and managing routing configurations.

## Features

- **Send Emails**: Allows users to send emails by entering the sender's and recipient's email addresses (local part only), subject, and body text.
- **Create Routes**: Users can create new routing rules for incoming emails.

## Requirements

- Python 3.x
- PyQt5
- requests

## Installation

Before running the application, ensure that Python 3.x is installed on your system. Then, install the required packages using pip:

```bash
pip install PyQt5 requests
```

## Usage

Run the application by executing the main Python script:

```bash
python email_manager.py
```

Once the application is running, you will see a window where you can input email details and create routes. The domain and API key for the Mailgun service are preconfigured.

### Sending an Email

1. Enter the local part of the sender's and recipient's email addresses. The domain part is pre-filled.
2. Type in the subject and body of the email.
3. Click on the "Send Email" button.

### Creating a Route

- Click on the "Create Route" button to create a new route with predefined settings.

## Configuration

- The Mailgun API key and domain are set in the code. Replace them with your actual Mailgun API key and domain.

```python
self.api_key = "your-mailgun-api-key" set them as env in your bashrc 
self.domain = "your-mailgun-domain.com"
```

- Modify the `create_route` method in the script to change routing rules as needed.

