from django.contrib import admin
from django.urls import path, include

from user import urls
from All_In_One import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from  food import views

urlpatterns = [

    path('upload_food_category/', views.UploadFoodCategory.as_view(), name='upload_food_category'),
    path('open_restaurent/<str:pk>', views.open_restaurent, name='open_restaurent'),
    path('view_food/<str:pk>',views.view_food,name='view_food'),
    # path('UploadFood/',views.UploadFood.as_view(),name='UploadFood'),

    path('restarent_register/', views.restarent_register, name='restarent_register'),
    path('restarent_login/',views.restarent_login,name='restarent_login'),
    path('restaurent_dashboard/',views.restaurent_dashboard,name='restaurent_dashboard'),
    path('addfooditem/',views.add_food,name='addfooditem'),
    path('add_food_to_cart/<str:pk>',views.add_food_to_cart,name='add_food_to_cart')
    
    #path('view_restaurents/',views.view_restaurents,name='view_restaurents')
   
    
#     path('display_categeory/', views.displaycategory, name='display_categeory'),
#     path('cloths_products/<int:pk>', views.cloths_products, name='cloths_products'),
#     path('openit/<int:pk>', views.openit, name='openit'),
#     path('addittocart/<int:pk>', views.addittocart, name='addittocart'),
#     path('success/', views.success, name='success'),
# path('fail/', views.fail, name='fail'),
#     path('view_cart/',views.view_cart,name='view_cart'),
#     path('reove_cart_item/<int:pk>',views.reove_cart_item,name='reove_cart_item'),
#     # path('addittocart_from_qty/',views.addittocart_from_qty,name='addittocart_from_qty'),
#     # path('update_qty/<int:pk><str:id>',views.update_qty,name='update_qty'),
#     path('buy_item/<int:pk>',views.buy_item,name='buy_item'),
#     path('Shipping/<int:pk>',views.save_address,name='Shipping'),
#     path('complete/', views.paymentComplete, name="complete"),
#     path('grand_checkout/',views.grand_checkout,name='grand_checkout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
