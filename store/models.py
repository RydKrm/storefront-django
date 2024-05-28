from django.db import models

# Create your models here.
class Product(models.Model):
    title =models.CharField(max_length=255) #
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

MEMBERSHIP_CHOICES = [
        ('B','Bronze'),
        ('S','Silver'),
        ('G', 'Gold')
    ]

class Customer(models.Model):
    first_Name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    birth_date = models.DateField(null=True)
    membership_choices = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')

PAYMENT_STATUS_CHOICES = [
    ('P', "Pending"),
    ('C', "Complete"),
    ('F', "Failed")
]    

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default='P')