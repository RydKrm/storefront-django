from rest_framework import serializers
from .models import Product,Collection, Customer
from decimal import Decimal
from datetime import date

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField
#     title = serializers.CharField(max_length = 255)
#     unit_price = serializers.DecimalField(max_digits=6,decimal_places=2, source='price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # * To see the collection  all field 
#     # collection = CollectionSerializer()
#     collection = serializers.HyperlinkedRelatedField(
#         queryset = Collection.objects.all(),
#         view_name='collection-detail'
#     )

#     def calculate_tax(self, product:Product):
#         return product.price * Decimal(1.1 ) 
    
#     def validate(self, data):
#         if len(data['title'])==0:
#             return serializers.ValidationError("title field is empty")
#         return data

# * product model serializer 
class ProductModelSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id','title','price','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self,product:Product):
        return product.price * Decimal(1.2)
    
    

# * product serializer 
class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id','title','slug','inventory','price','description']   

    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product

    def update(self,instance, validated_data):
        instance.price = validated_data.get('unit_price')
        instance.save()
        return instance 

class CustomerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Customer 
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'membership_choices','age']

    def get_age(self, customer:Customer):
        age = (date.today() - customer.birth_date)/(60*60*1000*24)
        return age    

    # def get_age(self, obj):
    #     if obj.birth_date:
    #         today = date.today()
    #         age = today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
    #         return age
    #     return None

# class CustomerSerializer(serializers.Serializer):
#     class Meta:
#         model = Customer
#         fields = ['id','first_name','last_name','email','phone','birth_date', 'membership_choices']
#         age = serializers.SerializerMethodField(method_name='calculate_age')

#         def calculate_age(self,customer:Customer):
#             age = date.today() - customer.birth_date
#             return age