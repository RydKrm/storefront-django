from django.urls import path
from . import views
# from views import person

# URLConf
urlpatterns = [
    path("hello", views.say_my_name),
    path("your_name",views.say_your_say),
    path("hello_world", views.hello_world)
] 