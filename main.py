from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
import sys
import requests
import os
class EmailManager(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("YOUR_API_KEY")
        self.domain = "YOUR_DOMAIN"
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setupInputFields(layout)
        self.setupButtons(layout)
        self.setLayout(layout)
        self.setupWindow()

    def setupInputFields(self, layout):
        self.from_email_input = QLineEdit(self)
        self.to_email_input = QLineEdit(self)
        self.subject_input = QLineEdit(self)
        self.text_input = QLineEdit(self)

        layout.addWidget(QLabel('From Email:'))
        layout.addWidget(self.from_email_input)
        layout.addWidget(QLabel('To Email:'))
        layout.addWidget(self.to_email_input)
        layout.addWidget(QLabel('Subject:'))
        layout.addWidget(self.subject_input)
        layout.addWidget(QLabel('Text:'))
        layout.addWidget(self.text_input)

    def setupButtons(self, layout):
        self.send_button = QPushButton('Send Email', self)
        self.create_route_button = QPushButton('Create Route', self)
        layout.addWidget(self.send_button)
        layout.addWidget(self.create_route_button)
        self.send_button.clicked.connect(self.send_email)
        self.create_route_button.clicked.connect(self.create_route)

    def setupWindow(self):
        self.setWindowTitle('Email Management System')
        self.setGeometry(300, 300, 300, 200)

    def send_email(self):
        from_email = self.from_email_input.text() + '@' + self.domain
        to_email = self.to_email_input.text()
        subject = self.subject_input.text()
        text = self.text_input.text()

        response = self.make_mailgun_request('messages', {
            "from": from_email,
            "to": to_email,
            "subject": subject,
            "text": text
        })
        QMessageBox.information(self, 'Email Sent', response)

    def create_route(self):
        response = self.make_mailgun_request('routes', {
            "priority": 0,
            "description": "New route",
            "expression": f"match_recipient('.*{self.domain}')",
            "action": ["forward('your-email@gmail.com')", "stop()"]
        })
        QMessageBox.information(self, 'Route Created', response)

    def make_mailgun_request(self, endpoint, data):
        url = f"https://api.mailgun.net/v3/{self.domain}/{endpoint}"
        try:
            response = requests.post(url, auth=("api", self.api_key), data=data)
            return response.text
        except Exception as e:
            return str(e)

app = QApplication(sys.argv)
email_manager = EmailManager()
email_manager.show()
sys.exit(app.exec_())
