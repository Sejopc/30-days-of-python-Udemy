import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "jpperaltac2@gmail.com"
password = "Qwaszx12!"
#---
from_email = username
to_list = ["jpperaltac@gmail.com"] # My primary Gmail account
#---
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password) # Make sure your email account has "Less secure apps" option enabled. Otherwise
                                         # you won't be able to login even with the right creds.
                                         # https://www.google.com/settings/security/lesssecureapps

    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello there!"
    the_msg['From'] = from_email
    #the_msg['To'] = to_list

    plain_text = "Plaintext message"
    html_text = """\
    <html>
        <head></head>
        <body>
            <p>Hey!<br>
            Testing this email <b>message</b>. Made by <a href='http://joincfe.com'>Team CFE</a>.
            </p>
        </body>
    </html>
    """

    part_1 = MIMEText(plain_text, 'plain')
    part_2 = MIMEText(html_text, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    # print(the_msg.as_string()) # Uncomment to see the MIME Body that will be send to the mail server.
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
    print("Email Sent Successfully.")

except smtplib.SMTPException:
    print("Error sending the message...")
