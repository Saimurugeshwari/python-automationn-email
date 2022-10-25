import smtplib, ssl

sender = 'ptest20002@gmail.com'
password = 'ploogcbkeyihzyfk'
receiver = 'ptest20002@gmail.com'

body_msg = '''subject: Hi, This is my first automation email
using smtplib.'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)