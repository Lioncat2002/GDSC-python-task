
import smtplib, ssl
from dotenv import load_dotenv
import os
import datetime
import csv
from apscheduler.schedulers.background import BackgroundScheduler
import tzlocal

def send_email(receiver_email,name):
    print('Called!')
    port = 465  # For SSL
    load_dotenv()
    password = os.getenv('PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = "away62159@gmail.com"
    #receiver_email = "gamedevcorp2002@gmail.com"
    message = f'Happy Birthday! {name}'
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("away62159@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)



def check_bday():
    csv_read=csv.DictReader(open('bdays.csv'))
    today=datetime.datetime.now().strftime('%d-%m')
    print(today)

    for i in csv_read:
        print(i['birthday'])
        birthday=i['birthday'].split('-')
        birthday=birthday[0]+'-'+birthday[1]
        if birthday==today:
            send_email(i['email'],i['name'])



scheduler=BackgroundScheduler(timezone=str(tzlocal.get_localzone()))

scheduler.add_job(check_bday, trigger='cron',hour='8-22', minute='*')
scheduler.start()

