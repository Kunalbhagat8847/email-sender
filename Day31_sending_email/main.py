import smtplib
import datetime as dt
import random

my_email="kbbhagat78@gmail.com"
password="Kunal@8847"

now=dt.datetime.now()
weekday=now.weekday()
# select tuesday
if weekday==1:
    with open("quotes.txt") as quote:
        all_quote=quote.readlines()
        random_quote=random.choice(all_quote)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bhagatdeepanshu2001@gmai.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}")


























# import smtplib
#
# my_email="Kunalbhagat8847@gmail.com"
# password="Kunal@884754"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # starttls used for transport layer security
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="Testmail@gmail.com",msg="Subject:Hello\n\nThis is the body of my email")
#
#

# import  datetime as dt
#
# now=dt.datetime.now()
# year=now.year
# print(year)