from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime

class Make(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.make.name + " " + self.name
    
class EngineType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.type

class Offer(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    description = models.CharField(max_length=512)
    engine_size = models.IntegerField(default=0)
    engine_power = models.IntegerField(default=0)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)

    phone_number = models.IntegerField(default=0)
    location = models.CharField(max_length=128, default="")

    production_date = models.DateField(default=datetime.now())
    publication_date = models.DateTimeField(default=datetime.now())
    
    def __str__(self) -> str:
        return self.model.make.name + " " + self.model.name + " " + str(self.price)
    
def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "images/" + str(instance.offer.pk) + "/" + filebase + "." + extension

class OfferImage(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    isMain = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_location)