from django.contrib import admin
from .models import  FoodCategory,RestaurentModel,ItemFood, FoodCart

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(RestaurentModel)
admin.site.register(ItemFood)
admin.site.register(FoodCart)
