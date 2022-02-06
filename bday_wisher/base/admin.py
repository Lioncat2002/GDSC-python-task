from pyexpat import model
from django.contrib import admin
from . import models

#registering the model so that it can appear on the admin panel
admin.site.register(models.Bday)
