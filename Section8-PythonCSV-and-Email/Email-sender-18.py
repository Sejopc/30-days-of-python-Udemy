import smtplib

host = "smtp.gmail.com"
port = 587
username = "jpperaltac2@gmail.com"
password = "Qwaszx12!"
#---
from_email = username
to_list = ["jpperaltac@gmail.com"] # My primary Gmail account

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password) # Make sure your email account has "Less secure apps" enabled. Otherwise
                                     # you won't be able to login even with the right creds.
                                     # https://www.google.com/settings/security/lesssecureapps
email_conn.sendmail(from_email, to_list, "Hello there, this is an email message")
email_conn.quit()

# ANOTHER WAY

from smtplib import SMTP

email_conn2 = SMTP(host, port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username, password) # Make sure your email account has "Less secure apps" enabled. Otherwise
                                     # you won't be able to login even with the right creds.
                                     # https://www.google.com/settings/security/lesssecureapps
email_conn2.sendmail(from_email, to_list, "Hello there, this is an email message too")
email_conn2.quit()

# NOW USING EXCEPTIONS
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong_password") # Make sure your email account has Less secure apps\ enabled. Otherwise
                                     # you won't be able to login even with the right creds.
                                     # https://www.google.com/settings/security/lesssecureapps
    pass_wrong.sendmail(from_email, to_list, "Hello there, this is an email message too")
except SMTPAuthenticationError:
    print("Incorrect Credentials.")
except:
    print("En error occured.")
pass_wrong.quit()
