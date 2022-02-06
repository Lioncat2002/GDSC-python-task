
import smtplib, ssl
from dotenv import load_dotenv
import os
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import Bday

#This is where the magic happens

#this function is used to send emails via SMTP 
#using the built in smtp lib of python
def send_email(receiver_email,name):
    port = 465  # For SSL
    load_dotenv()
    password = os.getenv('PASSWORD')

    print(f'Sending email to {receiver_email}')
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = os.getenv('EMAIL')
    message = f'Happy Birthday! {name}'
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("away62159@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent!')


#Checks if a person has birthday on a particular day
#Runs once perday
def check_bday():
    bdays=Bday.objects.all()
    today=datetime.datetime.now().strftime('%Y-%m-%d')
    print('Today:',today)
    #Extracting the day and month from today's date
    today=today.split('-')[2]+'-'+today.split('-')[1]
    

    for i in bdays:
        print(today)
        birthday=i.bday.strftime('%Y-%m-%d')
        #extracting day and month from the birthday
        birthday=birthday.split('-')[2]+'-'+birthday.split('-')[1]
        
        if birthday==today:
            send_email(i.email,i.name)





