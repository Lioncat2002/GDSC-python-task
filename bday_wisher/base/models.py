from django.db import models
#The birthday model
#Defines the format in which data will be stored in the database
class Bday(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(null=False,blank=False)
    bday=models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
      ordering=['-created']

    def __str__(self):
        return self.name+" created on: "+str(self.created.date())


