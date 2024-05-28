from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_my_name (request):
    return HttpResponse("You are heigenbgug")
   
def say_your_say(request):
    return HttpResponse("you are not good")

def hello_world(request):
    return render(request,'hello.html')