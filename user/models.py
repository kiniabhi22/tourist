from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    days=models.IntegerField()
    cost=models.IntegerField()
    offer=models.BooleanField()
    image=models.ImageField(upload_to="city" )
    

#we'll store all the data that we're entering in respective variables.


