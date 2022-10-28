from dataclasses import field, fields
from decimal import Clamped
from django import forms
from food.models import RestaurentModel, FoodCategory



class RestaurentForm(forms.ModelForm):
    class Meta:
      model=RestaurentModel
      fields=('rest_name','rest_image','rest_type','rest_city','rest_state',
      'rest_ratings','rest_pincode','rest_address',)
        
      # rest_name=forms.CharField(max_length=100)
      # rest_type = forms.CharField(max_length=100)
      # rest_city = forms.CharField(max_length=100)

      
      # rest_state = forms.CharField(max_length=100)
      
      # rest_image = forms.FileField(max_length=100)
      # rest_ratings =forms.CharField(max_length=100)
      # rest_pincode = forms.CharField(max_length=100)
      # rest_address = forms.CharField(max_length=100)
        # rzip = forms.CharField(max_length=100)
      exclude = ['rest_username','food_category','rest_status','rest_id','created_by']


class FoodForm(forms.ModelForm):
      class Meta:
        model=FoodCategory
        fields="__all__"
