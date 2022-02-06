# Birth Day Wisher
 A django app to wish happy birthday to your friends
# Requirements:
1. Django 4 or later for the front end
2. python-dotenv for loading environment variables
3. Apscheduler for scheduling the tasks
4. A throwaway gmail account

# How to run?
1. Insatll the dependencies with `pip install -r requirements.txt`
2. Make a Google account and turn ON [Access to less secure Apps](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OxzN10fD3e7RIkhq9GRiN2deXzACZjgQNc2F7m9FcH0eh1dlFTcim4cmuPds4qa2HOmcW-q2Ew8Hku1QldRkCE9AlAPA) (this requires 2FA to be disabled)
3. Make an environment variable called `.env` and information in the following format:
```
PASSWORD=<PASSWORD>
EMAIL=<EMAIL>
```
without the angle brackets
4. Run the App with `python manage.py runserver`

If you just want to look at how the email sender works, check out `testing.py`
