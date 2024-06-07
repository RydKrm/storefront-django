#### For creating a admin/superuser
python3 manage.py createsuperuser

then in `settings.py` add 
  ```python
  INSTALLED_APPS = [
    ...
    'django.contrib.sessions'
    ...
]
```

#### For changing the admin panel header title
In `urls.py` add this line over `urlpatterns`
 `admin.site.site_header = header name`


#### For register models into the admin panel

In `admin.py` add this line 
First import all the model then added 
```python
from . import models
admin.site.register(models.Collection)
```

#### For displaying product list in the model 

In `admin.py` add this 

```python 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price']
```