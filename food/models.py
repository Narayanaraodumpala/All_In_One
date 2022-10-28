from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def foodcatFile(instance, filename):
    return '/'.join(['category', str(instance.id), filename])


def foodFile(instance, filename):
    return '/'.join(['food', str(instance.id), filename])

def restaurent_iamge(instance, filename):
    return '/'.join(['restaurent', str(instance.id), filename])

def food_item_image(instance,filename):
    return '/'.join(['food',str(instance.id), filename])


class FoodCategory(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    category = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to=foodcatFile,
                                       max_length=254, blank=True, null=True)
    discount=models.CharField(max_length=3)

    class Meta:
        db_table = 'FoodCategory'

    def __str__(self):
        return self.category



class RestaurentModel(models.Model):
    rest_id=models.CharField(max_length=30)
    created_by=models.CharField(max_length=30,null=True)
    rest_username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    food_category=models.CharField(max_length=15,null=True)
    rest_status=models.CharField(max_length=10)
    rest_name=models.CharField(max_length=30)
    rest_image=models.ImageField(upload_to=restaurent_iamge,
                                       max_length=254, blank=True, null=True)
    rest_type=models.CharField(max_length=36,null=True)
    rest_city=models.CharField(max_length=20,null=True)
    rest_state=models.CharField(max_length=20,null=True)
    rest_ratings=models.CharField(max_length=3,null=True,default=2.5)
    rest_pincode=models.IntegerField(null=False,default=False)
    rest_address=models.CharField(max_length=50,null=False,default=False)

    class Meta:
        db_table='Restaurents'
   

    def __str__(self):
        return self.rest_name



class ItemFood(models.Model):
    fid=models.CharField(max_length=50)
    restaurent_name=models.CharField(max_length=50,null=True)
    restaurent=models.ForeignKey(RestaurentModel,on_delete=models.CASCADE,null=True)
    item=models.CharField(max_length=40,)
    item_type=models.CharField(max_length=19)
    item_price=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='available')
    image=models.FileField (upload_to=food_item_image,null=True)
    food_item_category = models.CharField(max_length=30,null=True)
    #food_item_category=models.ForeignKey(FoodCategory,on_delete=models.CASCADE,null=True)
    item_ratings=models.CharField(max_length=10)
   

    class Meta:
        db_table='FoodItems'


    def __str__(self):
        return self.item

class FoodCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(ItemFood,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    
    class meta:
        db_table="FoodCartItems"
        
    def __str__(self) :
        return self.item.item