from django.db import models

# Promotion many-to-many relationship
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

# Create your models here.
class Product(models.Model):
    title =models.CharField(max_length=255) 
    slug = models.SlugField( )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) 
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)  
    promotions = models.ManyToManyField(Promotion)


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
    # class Meta:
    #     db_table = 'store_customers'
    #     index = [
    #         models.Index(fields=["last_name","first_name"])
    #     ]


PAYMENT_STATUS_CHOICES = [
    ('P', "Pending"),
    ('C', "Complete"),
    ('F', "Failed")
]    

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)    

# One-to-Many relationship
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    crated_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()        