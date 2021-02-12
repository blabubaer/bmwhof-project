from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class Part(models.Model):
    part_number =       models.CharField(max_length=255)
    name =              models.CharField(max_length=255)
#correct later
    category =          models.CharField(max_length=255)
#correct later
    car_model =         models.CharField(max_length=255)
    count =             models.IntegerField()
    description =        models.TextField(max_length=255)
    image =             models.ImageField(upload_to='parts/images/', blank=True)
    datecreated =       models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




