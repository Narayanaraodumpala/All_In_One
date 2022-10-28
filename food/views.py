import json
from os import fchdir
from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import render, redirect
from food.models import FoodCategory, RestaurentModel, ItemFood, FoodCart
from rest_framework.generics import ListAPIView
from .serializers import FoodCatSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import View
from food.forms import RestaurentForm


import random
import string


import random
import string


# Create your views here.


def restarent_register(request):
    print('---')
    def random_string(length=8, uppercase=True,
                      lowecase=True, numbers=True):
        charecter_set = '-'
        if uppercase:
            charecter_set += string.ascii_uppercase
        if lowecase:
            charecter_set += string.ascii_lowercase
        if numbers:
            charecter_set += string.digits
        return ''.join(random.choice(charecter_set) for i in range(length))

    my_random = random_string(8)
    unique_rest_id = '#R1'+my_random
    print('unique_food_id=', unique_rest_id)

    if request.method == "POST":
        # print('sdtx t f g y')
        dic = request.POST
        rid = unique_rest_id

        print('rid=', rid)
        fcat = request.POST['fcat']
        runame = dic['rusername']
        rname = dic['rname']
        rimg = request.FILES['rimage']
        print(rimg)

        print('fcat=', fcat)
        rtype = dic['rtype']
        rststa = dic['rstate']
        rcity = dic['rcity']
        rzip = dic['rzip']

        remail = dic['remail']

        rpwd = dic['rpassword']
        raddress = dic['raddress']

        rstatus = 'Pending'
        restaurent_data = User.objects.filter(username=runame)
        print('fetching done')
        print(restaurent_data)
        if not restaurent_data:

            rest_user = User.objects.create_user(
                username=runame, email=remail, password=rpwd)
            print('user saved')
            usr = request.user
            if usr:
                created_by = usr
            else:
                created_by = runame
            instance = RestaurentModel.objects.create(rest_username=rest_user, created_by=created_by, rest_name=rname,
                                                      rest_image=rimg, food_category=fcat,
                                                      rest_status=rstatus,
                                                      rest_id=rid, rest_type=rtype, rest_state=rststa,
                                                      rest_city=rcity, rest_pincode=rzip, rest_address=raddress)

            print('restaurent saved')

            return redirect('restarent_login')

        else:
            print('user not saved')
            error = True
            print('error is thhre')

    return render(request, 'restaurent/restaurant_register.html', {'error': error})


class UploadFoodCategory(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCatSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = FoodCategory.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


def open_restaurent(request, pk):

    res = RestaurentModel.objects.filter(food_category=pk)

    return render(request, 'food/open_restaurent.html', {'res': res})


def view_food(request, pk):
    print('pk for viewfood=', pk)
    res = RestaurentModel.objects.filter(rest_id=pk)
    restres = RestaurentModel.objects.filter(rest_id=pk).first()
    print('restaurent details=', res)
    print('user=', restres.rest_username)
    food = ItemFood.objects.filter(restaurent_name=restres.rest_username)
    print('food items=', food)
    vegfood = ItemFood.objects.filter(
        restaurent_name=restres.rest_username, item_type='veg')
    print('vegfood items=', vegfood)
    Nonvegfood = ItemFood.objects.filter(
        restaurent_name=restres.rest_username, item_type='Non-veg')
    print('nonvegfood items=', Nonvegfood)
    dessertfood = ItemFood.objects.filter(
        restaurent_name=restres.rest_username, item_type='dessert')
    print('nonvegfood items=', dessertfood)

    return render(request, 'food/view_food.html', {'rest_res': res, 'food': food, 'vegfood': vegfood,
                                                   'Nonvegfood': Nonvegfood, 'dessertfood': dessertfood})


# from food.serializers import FoodSerializer

# class UploadFood(ListAPIView):
#     queryset = FoodModel.objects.all()
#     serializer_class = FoodSerializer

#     def post(self, request, *args, **kwargs):
#         file = request.data['file']
#         fid=unique_food_id
#         image = FoodModel.objects.create(image=file,fid=fid)
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


def restarent_login(request):
    if request.user.is_authenticated:
        return redirect('restaurent_dashboard')
    else:
        error = False

        if request.method == 'POST':
            dic = request.POST
            ruser = dic['ruser']
            rpassword = dic['rpassword']
            print(ruser)
            data = User.objects.filter(username=ruser).first()
            print(data)

            user = authenticate(username=ruser, password=rpassword)
            print(user)

            if not data:
                print('-----')
                message = 'incorrect username'
                print(message)
                return render(request, 'food/restarent_login.html', {'user_mesg': message})
            else:

                if not data.is_active:
                    message = 'account not verified'
                    return render(request, 'food/restarent_login.html', {'message': message})

                else:

                    if user:
                        login(request, user)
                        return redirect('restaurent_dashboard')
                    # return render(request,'food/restaurent_dashboard.html',{'res':FoodCategory.objects.all})
                    else:
                        error = True
    return render(request, 'food/restarent_login.html')


def restaurent_dashboard(request):
    user = request.user
    print('restaurent login=', user)
    rest_data = RestaurentModel.objects.filter(rest_username=user)
    print('rest_data=', rest_data)
    fcount = ItemFood.objects.filter(restaurent_name=request.user).count()
    return render(request, 'food/restaurent_dashboard.html', {'rest_data': rest_data, 'res': FoodCategory.objects.all(),
                                                              'food': ItemFood.objects.filter(restaurent_name=request.user), 'fcount': fcount})


def add_food(request):
    def random_string(length=8, uppercase=True,
                      lowecase=True, numbers=True):
        charecter_set = '-'
        if uppercase:
            charecter_set += string.ascii_uppercase
        if lowecase:
            charecter_set += string.ascii_lowercase
        if numbers:
            charecter_set += string.digits
        return ''.join(random.choice(charecter_set) for i in range(length))

    random_food_id = random_string(8)
    unique_food_id = '#F1'+random_food_id
    print('unique_food_id=', unique_food_id)

    if request.method == "POST":
        item = request.POST['item']
        restaurent_name = request.user
        fid = unique_food_id
        item_type = request.POST['itemtype']
        item_price = request.POST['price']
        status = request.POST['status']
        image = request.FILES['item_image']
        food_item_category = request.POST['fcat']
        item_ratings = request.POST['ratings']
        print('food_item_category=', food_item_category)
        foodcategory = FoodCategory.objects.filter(
            category=food_item_category).first()

        print('foodcategory=', foodcategory)
        restaurent=RestaurentModel.objects.get(rest_username=request.user)
        ItemFood.objects.create(item=item, restaurent_name=restaurent_name,restaurent=restaurent, fid=fid,
                                item_type=item_type, item_price=item_price, status=status,
                                image=image, food_item_category=food_item_category, item_ratings=item_ratings)
        print('food data saved successfully')
        return redirect('restaurent_dashboard')


def add_food_to_cart(request, pk):
    print('pk=', pk)
    # if request.method == "POST":
    #     qty = request.POST['quantity']
    #     print('qty=', qty)
    #     food_data = ItemFood.objects.filter(fid=pk)
    #     print('food_data=', food_data)

    #     pass
    
    itemdata=ItemFood.objects.get(fid=pk)
    print('itemdata=',itemdata)
    iprice=itemdata.item_price
    print('item price=',iprice)
    usr = request.user
    cartdata=FoodCart.objects.filter(user=usr,item=itemdata)
    print('cartdata=',cartdata)

    if request.method == 'POST':

       item_price = itemdata.item_price

       quantity = request.POST['quantity']
       
       total = int(item_price) * int(quantity)
       print('total_price=',total)
       if cartdata:
         
           
            restaurent=ItemFood.objects.get(fid=pk)
           
            print('reusname=',restaurent.restaurent.rest_username)

            rest_i=restaurent.restaurent.rest_id
           
            restres = RestaurentModel.objects.get(rest_id=rest_i)
            
            print('restaurent details=', restres)
            rest_name=restres.rest_username
            print('restname=',rest_name)
            food = ItemFood.objects.filter(restaurent_name=rest_name)
            print('food items=', food)
            vegfood = ItemFood.objects.filter(
                restaurent_name=rest_name, item_type='veg')
            print('vegfood items=', vegfood)
            Nonvegfood = ItemFood.objects.filter(
                restaurent_name=rest_name, item_type='Non-veg')
            print('nonvegfood items=', Nonvegfood)
            dessertfood = ItemFood.objects.filter(
                restaurent_name=rest_name, item_type='dessert')
            print('nonvegfood items=', dessertfood)
                

            return render(request, 'food/view_food.html',{'message':'Sorry, this item has already been put to your cart. Please double check the quantity in your cart , or add another item.',
                                                          'res': restres,'vegfood': vegfood,  'Nonvegfood': Nonvegfood, 'dessertfood': dessertfood})
       else:
           FoodCart.objects.create(user=usr, item=itemdata, quantity=quantity,total_price=total)

    return redirect('view_cart')



