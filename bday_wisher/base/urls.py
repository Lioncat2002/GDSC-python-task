from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path
from apscheduler.schedulers.background import BackgroundScheduler
import tzlocal
from .email_sender import check_bday

#Setting the urls
urlpatterns = [
    #home url
    path('',views.homeView,name='home'),
    #birthday form url
    path('bdayform',views.addBday,name='bday')
    
]

#Setting the email to be executed everyday
#Setting the scheduler here since urls.py executed once at the start of the app
scheduler=BackgroundScheduler(timezone=str(tzlocal.get_localzone()))
#hour 8-22 means that the function will be called between 8 in morning till 22 at night
#minute=* means that the function will be executed every minute
#we might get a warning when second=* since sending the email takes longer than a second
scheduler.add_job(check_bday, trigger='cron',hour='7-22',second='*')
scheduler.start()