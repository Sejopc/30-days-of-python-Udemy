import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "jpperaltac2@gmail.com"
password = "Qwaszx12!"
from_email = username
#to_list = ["jpperaltac@gmail.com"]

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}!,

    Thank you for the purchase on {date}!
    We hope you are exicted about using it. Just as a reminder,
    the purchase total was ${total}.

    Have a great one,

    Team CFE.
    """
    def add_user(self, name, amount, email=None):
        name = name.lower().capitalize()
        amount = "%.2f" % (amount)
        detail = {
            "name":name,
            "amount":amount
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_message = message.format(name=name, date=date, total=amount)
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_message
                    }
                    self.email_messages.append(user_data)
                else:
                    self.message.append(new_message)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                # run email here
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)

                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing update!"
                    the_msg['From'] = from_email
                    the_msg['To'] = user_email
                    part_1 = MIMEText(user_message, 'plain')

                    the_msg.attach(part_1)

                    # print(the_msg.as_string()) # Uncomment to see the MIME Body that will be send to the mail server.
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                    print("Email Sent Successfully.")

                except smtplib.SMTPException:
                    print("Error sending the message...")
            return True
        return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email="jpperaltac2@gmail.com")
obj.add_user("John", 4213.33, email="jpperaltac2@gmail.com")
obj.add_user("Emilee", 2500.00, email="jpperaltac2@gmail.com")
obj.add_user("Jim", 123.00, email="jpperaltac2@gmail.com")
obj.add_user("Ron", 342.00, email="jpperaltac2@gmail.com")
obj.add_user("Sandra", 8239.34, email="jpperaltac2@gmail.com")
obj.get_details()
obj.send_email()
