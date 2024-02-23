from django.db import models
from enum import Enum

class UserRole(Enum):
    DONOR = 'donor'
    CHARITY = 'charity'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[(role.value, role.name) for role in UserRole])
    EIN_Number = models.CharField(max_length=255)
    image_data = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Charity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    image_data = models.CharField(max_length=255)
    description = models.TextField()
    inventory = models.IntegerField()
    pick_up_deadline = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartedDonation(models.Model):
    id = models.AutoField(primary_key=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    donation_receipt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DonationCategory(models.Model):
    id = models.AutoField(primary_key=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
