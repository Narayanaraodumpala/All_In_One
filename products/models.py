
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserManager


# Create your models here.


def catFile(instance, filename):
    return '/'.join(['category', str(instance.id), filename])


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to=catFile,
                                       max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.category


def productFile(instance, filename):
    return '/'.join(['products', str(instance.id), filename])


class Cloths(models.Model):
    product_id = models.CharField(max_length=30, unique=True)
    product_name = models.CharField(max_length=150, unique=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to=productFile,
                                      max_length=254, blank=True, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return self.product_name


class Addtocart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    product = models.ForeignKey(Cloths, on_delete=models.CASCADE, related_name='cloths')
    quantity = models.IntegerField()
    total_price=models.FloatField(null=True)

    objects = UserManager()

    class Meta:
        db_table = 'CartItems'

    def __str__(self):
        return self.product.product_name


class OrderAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ship_user')
    name = models.CharField(max_length=256, blank=True)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=8,null=True)
    address=models.CharField(max_length=56, blank=True)
    street_or_landmark =models.CharField(max_length=56, blank=True)
    city=models.CharField(max_length=56, blank=True)
    state=models.CharField(max_length=56, blank=True)
    postal_code=models.CharField(max_length=8)

    

    class Meta:
        db_table = 'ShippingAddress'

    def __str__(self):
        return self.user.username
    
    
class Orders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    #shipping=models.ForeignKey(OrderAddress, on_delete=models.CASCADE, related_name='shipping')
    product=models.ForeignKey(Addtocart,on_delete=models.CASCADE,related_name='order')
    
    
    class Meta:
        db_table="Orders"
        
    def __str__(self) :
        return self.product.product.product_name


