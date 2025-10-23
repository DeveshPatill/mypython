# Write your Python code here
from django.db import models
from django.contrib.auth.models import User

class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    preferred_payment_method = models.CharField(max_length=30)
    default_pickup_address = models.TextField()
    profile_image = models.ImageField(upload_to='riders/', null=True, blank=True)

    def __str__(self):
        # Return a string with the rider's name or phone
        return f"Rider: {self.user.username}"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=30)
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_plate_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='drivers/', null=True, blank=True)

    def __str__(self):
        # Return a string with the driver's name or license
        return f"Driver: {self.user.username}"