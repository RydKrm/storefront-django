from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models
from django.utils.html import format_html 
# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.Address)
admin.site.register(models.CartItem)
admin.site.register(models.Collection  )

# another way for registering model and  
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin): 
    # for adding data in the inventory 
    # fields = ['title','price']
    
    # for excluding value 
    exclude = ['promotion']

    # for read only fields
    # readonly_fields = ['title']

    # for automatic populated field
    prepopulated_fields = {
        'slug':['title']
    }

    # this list display in the table models
    list_display = ['title','price','inventory_status']
    # register action here
    actions = ['clear_inventory']
    # for search field
    search_fields = ['title','price ']
    # list_editable = ['title','price']
    list_per_page = 15
    # filtering items
    list_filter = ['collection','last_update']
    def inventory_status(self,product):
        if product.inventory <10:
            return 'Low'
        return "OK"
    # for adding extra action 
    @admin.action(description="clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} product were successfully updated  '
        )
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['first_name','last_name','membership_choices']
    # list_editable = ['first_name','last_name','membership_choices']
    list_per_page = 12

# @admin.register(models.Collection)
# For overriding the base query set 
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ['title','products_count']

#     @admin.display(ordering='products_count')
#     def products_count(self, collection):
#         return collection.products_count

#     def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
#         return super().get_queryset(request).annotate(
#             products_count = Count('product')
#         )     