# Write your Python code here
# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver

class RiderRegistrationSerializer(serializers.ModelSerializer):
    # Define custom fields
    phone_number = serializers.CharField()
    preferred_payment_method = serializers.CharField()
    default_pickup_address = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'preferred_payment_method', 'default_pickup_address']

    def create(self, validated_data):
        # Create user and Rider profile
        username = validated_data.pop("username")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        #create with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)

        # create driver profile
        rider = Rider.objects.create(user=user, **validated_data)
        return Rider


class DriverRegistrationSerializer(serializers.ModelSerializer):
    # Define custom fields
    phone_number = serializers.CharField()
    license_number = serializers.CharField()
    vehicle_make = serializers.CharField()
    vehicle_model = serializers.CharField()
    vehicle_plate_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'license_number',
                  'vehicle_make', 'vehicle_model', 'vehicle_plate_number']

    def create(self, validated_data):
        # Create user and Driver profile
        username = validated_data.pop("username")
        email = validated_data,pop("email")
        password = validated_data.pop("password")

        #create user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)

        #create driver profile
        driver = Driver.objects.create(user=user, **validated_data)
        return driver