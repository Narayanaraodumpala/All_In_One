from django.contrib import admin
from django.urls import path, include

from products import views
from user import urls
from All_In_One import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [

    path('upload_product/', views.UploadCloths.as_view(), name='upload_product'),
    path('display_categeory/', views.displaycategory, name='display_categeory'),    
    path('cloths_products/<int:pk>', views.cloths_products, name='cloths_products'),
    path('openit/<str:pk>', views.openit, name='openit'),
    path('addittocart/<str:pk>', views.addittocart, name='addittocart'),
    path('success/', views.success, name='success'),
    path('fail/', views.fail, name='fail'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('reove_cart_item/<str:pk>',views.reove_cart_item,name='reove_cart_item'),
    # path('addittocart_from_qty/',views.addittocart_from_qty,name='addittocart_from_qty'),
    # path('update_qty/<int:pk><str:id>',views.update_qty,name='update_qty'),
    path('buy_item/<str:pk>',views.buy_item,name='buy_item'),
    path('Shipping/<str:pk>',views.save_address,name='Shipping'),
    path('complete/', views.paymentComplete, name="complete"),
    path('grand_checkout/',views.grand_checkout,name='grand_checkout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
