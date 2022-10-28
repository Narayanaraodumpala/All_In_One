from itertools import product
import json

from .models import OrderAddress, Orders
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views import View

from rest_framework.generics import ListAPIView

import user
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from .models import Addtocart as AddtocartModel

from products.models import Cloths as ClothsModel, Category

from food.models import FoodCart


class UploadCloths(ListAPIView):
    queryset = ClothsModel.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = ClothsModel.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


def displaycategory(request):
    return render(request, 'home/dcategoriy.html', {'cloths': Category.objects.all()})

from django.core.paginator import Paginator, EmptyPage
def cloths_products(request, pk,page=1):
    # print('pk=',pk)
    # res=Cloths.objects.filter(product_category=pk)
    # print(res)

    # print(res.product_name)
    # print(res.price)
    # print(res.status)
    cloths= ClothsModel.objects.filter(product_category=pk).order_by('id')
    
    #cart=AddtocartModel.objects.filter(user=request).all()
    # for price in cart.total_price:
    #     gprice=price
    #page = request.GET.get('page', 1)
    #paginator = Paginator(cloths, 4)
    #try:
        #res = paginator.page(page)
    #except EmptyPage:
        # if we exceed the page limit we return the last page
        #res = paginator.page(paginator.num_pages)
    return render(request, 'cloths/product_cloths.html',
                  {'products': cloths, 'pk': pk})


def openit(request, pk):
    print('pk=', pk)
    res = ClothsModel.objects.filter(product_id=pk)
    print('res=', res)

    return render(request, 'cloths/throughtocart.html', {'res': res})


# class Addittocart(View):
#     def post(request,pk):
#         print(pk)
#         if request.method=='POST':
#             qty=request.POST.get('quantity')
#             print('qty=',qty)
#             res = ClothsModel.objects.filter(product_id=pk).first()
#             print(res.status)
#             if res.status == 'no ':
#                 print('-- yes')
#                 pass

#             else:
#                 print('---no')
#                 pass
#             pass

@login_required(login_url='login_signup')
def addittocart(request, pk, data=None):
    print(pk)
    if request.method == 'POST':
        qty = request.POST['quantity']
        print('qty=', qty)
        res = ClothsModel.objects.filter(product_id=pk).first()
        status = res.status
        print(status)
        print(res.product_name)
        if status == 'no' :
            error = 'sorry!, this product is not avialable at this time'
            print(error)
            return render(request, 'cloths/throughtocart.html',
                          {'error': error, 'pid': res.product_id, 'pname': res.product_name,
                           'pimg': res.product_image.url, 'pstat': res.status})
        elif qty >= str(1):
            print(type(res.price))
            total = float(qty) * float(res.price)
            print('toatlllll===', total)
            product = AddtocartModel.objects.filter(product=res, user=request.user)
            if not product:
                AddtocartModel.objects.create(user=request.user, product=res, quantity=qty, total_price=total)
                return redirect('success')
            else:
                return redirect('fail')
        else:

            msg = 'sorry! ensure quantity is 1 or more'
            print(msg)
            return render(request, 'cloths/throughtocart.html',
                          {'message': msg, 'pid': res.product_id, 'pname': res.product_name,
                           'pimg': res.product_image.url, 'pstat': res.status})


# def addittocart_from_qty(request):
#     pis=request.POST['pid']
#     qty=request.POST['quantity']
#
#     print('pid=',pis)
#     print('qty=',qty)
#     res = ClothsModel.objects.filter(product_id=pis)
#     print('res=',res)
#     if qty >= str(1):
#         return render(request, 'cloths/add.html')
#
#     else:
#
#         msg = 'sorry! ensure quantity is 1 or more'
#         print(msg)
#         return render(request, 'cloths/throughtocart.html',
#                       {'message': msg, 'res':res})
def success(request):
    return render(request, 'cloths/add.html')


def fail(request):
    return render(request, 'cloths/failure.html')


def view_cart(request):
    global total_price
    res = AddtocartModel.objects.filter(user=request.user)
    items = res

    total_price = sum(items.values_list(('total_price'), flat=True))
    print(total_price)
    
    foodcartitems=FoodCart.objects.filter(user=request.user)
    foodgrandtotal = sum(foodcartitems.values_list(('total_price'), flat=True))
    print('foodgrandtotal=',foodgrandtotal)

    return render(request, 'cloths/cart_items.html', {'res': res, 'total_price': total_price,'foodres':foodcartitems, 'foodgrandtotal':foodgrandtotal})


def reove_cart_item(request, pk):
    res = AddtocartModel.objects.filter(product__product_id=pk, user=request.user).delete()
    print('res=', res)
    return redirect('view_cart')


# def update_qty(request,pk,id):
#     print(pk)
#     res=AddtocartModel.objects.filter(product__product_id=pk, user=request.user)
#     print('id=',id)
#     data=AddtocartModel.objects.get(id=id)
#     print('tp=',data.total_price)


#     if request.method == "POST":
#         qty=request.POST['cart_qty']
#         total=float(price )* float(qty)
#         print('total=',total)
#         data=AddtocartModel(quantity=qty,total_price=total)
#         data.save()

#         print('its update')


def buy_item(request, pk):
    res = AddtocartModel.objects.filter(product__product_id=pk, user=request.user)
    data = OrderAddress.objects.filter(user=request.user).last()

    if data:
        id = data.id
        print('id=', id)
        # print('address=',data.name)
        return render(request, 'cloths/buy_item.html',
                      {'res': res, 'id': id, 'name': data.name, 'mobile': data.phone, 'address': data.address,
                       'email': data.email, 'gender': data.gender, 'street': data.street_or_landmark,
                       'city': data.city, 'state': data.state, 'postal_code': data.postal_code})
    else:
        # id = data.id
        # print('id=', id)
        OrderAddress.objects.create(user=request.user, name='null', email='null', phone=00,
                                    gender='null',
                                    address='null', street_or_landmark='null',
                                    city='null', state='null', postal_code='null')
        return render(request, 'cloths/buy_item.html', {'res': res})


def save_address(request, pk, res=None):
    if request.method == "POST":

        res = AddtocartModel.objects.filter(product__product_id=pk, user=request.user)

        data = request.POST
        name = data['name']
        # first_name=data['first-name']
        # last_name=data['last-name']
        email = data['email']
        phone_number = data['mobile']
        address = data['address']
        gender = data['gender']
        street = data['Street']
        city = data['city']
        state = data['state']
        post_code = data['pincode']
        OrderAddress.objects.create(user=request.user, name=name, email=email, phone=phone_number, gender=gender,
                                    address=address, street_or_landmark=street, city=city, state=state,
                                    postal_code=post_code)
        data = OrderAddress.objects.filter(user=request.user).last()
        print('data=', data.gender)
        return render(request, 'cloths/address.html',
                      {'res': res, 'name': data.name, 'mobile': data.phone, 'address': data.address,
                       'email': data.email, 'gender': data.gender, 'street': data.street_or_landmark,
                       'city': data.city, 'state': data.state, 'postal_code': data.postal_code})
    else:
        id = OrderAddress.objects.get(id=pk)

        if id:
            res = request.GET.get('res')
            pres = AddtocartModel.objects.filter(product__product_id=res, user=request.user)
            print('res=', pres)

            OrderAddress.objects.create(user=request.user, name=id.name, email=id.email, phone=id.phone,
                                        gender=id.gender,
                                        address=id.address, street_or_landmark=id.street_or_landmark,
                                        city=id.city, state=id.state, postal_code=id.postal_code)
            data = OrderAddress.objects.filter(user=request.user).last()

            return render(request, 'cloths/address.html',
                          {'res': pres, 'name': data.name, 'mobile': data.phone, 'address': data.address,
                           'email': data.email, 'gender': data.gender, 'street': data.street_or_landmark,
                           'city': data.city, 'state': data.state, 'postal_code': data.postal_code})




def paymentComplete(request):
    body = json.loads(request.body)
    print('---')
    product = AddtocartModel.objects.get(id=body['product_id'])
    print('body=', body)
    print('----')
    Orders.objects.create(user=request.user, product=product)
    print('wdey----')
    return JsonResponse('payment completed', safe=False)


def grand_checkout(request):
    # global gprice
    # cart=AddtocartModel.objects.filter(user=request.user).all()
    # print(cart.total_price)
    # for price in cart.total_price:
    #     print(price)
    #     gprice=gprice+price
    #     print(gprice)
    # grand=gprice
    # print(grand)

    pass
