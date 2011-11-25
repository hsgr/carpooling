from django.db import models
from django.contrib.auth.models import User

# Draft - fields differ from etherpad brainstorming 

class UserProfile(models.Model):
    firstName = models.CharField(max_length=100, verbose_name = "First Name")
    lastName = models.CharField(max_length=100, verbose_name = "Last Name")
    location = models.CharField(max_length=100, verbose_name = "Current Location")
    email = models.EmailField()
    phoneNum = models.IntegerField(max_length=100, verbose_name = "Phone Number")
    user = models.OneToOneField(User,parent_link=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

class Vehicle(models.Model):
    
    # license needs a more elegant way to define license plates eg: regexp
    licensePlate = models.CharField(max_length=6, verbose_name = "License Plate")
    availableSeats = models.IntegerField()
    STORAGE_CHOICES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra-Large'),
        )
    storageCompartment = models.CharField(max_length=1, choices=STORAGE_CHOICES)

# Following classes: Missing tons of details about routing 

class RouteRequest(models.Model):
    requester = models.OneToOneField(UserProfile) 
    requestOrigin = models.CharField(max_length=100)
    requestDestination = models.CharField(max_length=100)

class RouteOffer(model.Model):
    offerer = models.OneToOneField(UserProfile)
    offeredVehicle = models.OneToOneField(Vehicle)
    offerOrigin = models.CharField(max_length=100)
    offerDestination = models.CharField(max_length=100)




    
