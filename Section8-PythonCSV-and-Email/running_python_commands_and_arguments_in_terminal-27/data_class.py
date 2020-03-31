import csv
import datetime
import shutil
import os
from tempfile import NamedTemporaryFile
from utils.templates import get_template, render_context
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 3 different ways to call the folder that we are in:
file_item_path2 = os.path.join(os.path.dirname(os.path.abspath("data4.csv")))
file_item_path3 = os.path.join(os.path.dirname(__file__), "data4.csv") # here __file__ refers this python file (data_manager.py).
                                                                        # In other words, join the directory where this file exists
                                                                        # with "data4.csv".
file_item_path1 = os.path.join(os.getcwd(), file_item_path3)


host = "smtp.gmail.com"
port = 587
username = "jpperaltac2@gmail.com"
password = "Qwaszx12!"
from_email = username
to_list = []

class UserManager():

    def render_message(self, user_data):
        file_ = "templates/email_message.txt"
        file_html = "templates/email_message.html"
        template = get_template(file_)
        template_html = get_template(file_html)
        if isinstance(user_data, dict):
            context = user_data # user comes as a dictionary.
            plain_ = render_context(template, context)
            html_ = render_context(template_html, context)
            return(plain_,html_)
        return (None,None) # returned in case user_id and email are both None (not passed when the function is called.)

    def message_user(self, user_id=None, email=None, subject="Billing update!"):
        user = self.get_user_data(user_id=user_id, email=email)
        if user:
            plain_, html_ = self.render_message(user)
            print(plain_,html_)
            user_email = user.get('email', 'noreply@gmail.com') # it means: get the 'email' value from the user dictionary, if the 'email' key doesn't exist, then assign noreply@gmail.com to 'user_email' var.
            to_list.append(user_email)
            try:
                email_conn = smtplib.SMTP(host, port)
                email_conn.ehlo()
                email_conn.starttls()
                email_conn.login(username, password)

                the_msg = MIMEMultipart("alternative")
                the_msg['Subject'] = subject
                the_msg['From'] = from_email
                the_msg['To'] = user_email
                part_1 = MIMEText(plain_, 'plain')
                part_2 = MIMEText(html_, 'html')
                the_msg.attach(part_1)
                the_msg.attach(part_2)
            except smtplib.SMTPException:
                print("Error sending the message...")
            # print(the_msg.as_string()) # Uncomment to see the MIME Body that will be send to the mail server.
            email_conn.sendmail(from_email, to_list, the_msg.as_string())
            email_conn.quit()
            print("Email Sent Successfully.")
        return None # returned in case user_id and email are both None (not passed when the function is called.)


    #@staticmethod #-> used in case the calling script (.py) to this method didn't want to make an instance of UserManager class.
                    # but also realized is not necessarily at all. You can simply call this method using UserManager().get_user_data()
                    # without the need to create an instance of the class in advance (i.e f=UserManager(), f.get_user_data())

    def get_user_data(self, user_id=None, email=None):
        print("Directory: %s" % file_item_path3)
        print("Full path to CSV file: %s" % file_item_path1)
        file_name = file_item_path3
        with open(file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_user_id = None
            unknown_email = None
            for row in reader:
                if user_id is not None:
                    if str(user_id) == str(row.get("id")):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                print("User id {user_id} not found.".format(user_id=user_id))
            if unknown_email is not None:
                print("Email {email} not found.".format(email=email))
        return None
