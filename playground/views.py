from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Collection, Customer
from django.db.models import Q,F 
from django.db.models.aggregates import Count, Max, Min, Avg

# Create your views here.
def say_my_name (request):
    return HttpResponse("You are heigenbgug")
   
def say_your_say(request):
    return HttpResponse("you are not good")

def hello_world(request):
    return render(request,'hello.html')

def get_product(request):
    # try :
    #    singleProduct = Product.objects.get(pk=1) 
    # except ObjectDoesNotExist:
    #     pass

    # exists = Product.objects.filter(pk=1).exists();

    # * filtering object
    # productList = Product.objects.filter(price__range=(10, 300))
    # * get product where price is less than 100 and inventory is greatert than 3 

    # productList = Product.objects.filter(price__lt=100, inventory__gt=3)
      
    # * get product where price is less than 100 or inventory is grater than 3 whi Q object 
    # productList = Product.objects.filter(Q(inventory__lt=100) | Q(price__gt=100))

    # * F object using for field matching with another field 4
    # productList = Product.objects.filter(inventory=F('collection__id')) 

    # * Sorting data 
    # productList = Product.objects.order_by('-price')

    # * sort data according to price if price is same than sorting according to title reverse
    # productList = Product.objects.order_by('price', 'title').reverse()


    # * Limit the query object 
    productList = Product.objects.values('id','title','price','inventory','collection__title').order_by('price')[0:10]

    #  Aggregate Function 
    # productList = Product.objects.filter(price__gt=50).aggregate(total_product=Count('id'), min_price = Min('price'))

    # ? Aggregate functions

    # ? create a object 
    # customer = Customer()
    # customer.first_Name = "Riyad"
    # customer.last_name = "Karim"
    # customer.email = "rysd@gmail.com"
    # customer.phone = "01756165161"
    # customer.birth_date = '2006-12-06'
    # customer.save()
    
    # update a object
    # customer = Customer.objects.get(pk=101)
    # customer.first_Name = "Al Riyad "
    # customer.last_name = "karim"
    # customer.save()

    # Delete object 
    # collection = Collection(pk=101)
    # collection.delete()
     
    # Product.object.filter(price__lt=10).delete() 



    return render(request,'hello.html',{'title':"Product List between 10 to 30", 'products':list(productList)})


    # return HttpResponse("get product") 