"""
Set up email service for daily emailing
"""

import smtplib, ssl, time




def emailer(sender_email, sender_password, reciever, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email  # Enter your address
    receiver_email = reciever  # Enter receiver address
    password = sender_password
    message = message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever, message)


if __name__ == "__main__":
    message = "HI EVAN"

    emailer("coopmanmike@gmail.com",  , "macoopman@gmail.com", message)
