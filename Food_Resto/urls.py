"""
URL configuration for Food_Resto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Order.views import *#create_order,Open_order,Close_order,edit_order,view_order,print_order,cancel_order
from Shop_detail.views import *#home,add_shop_detail,add_product,list_product,edit_product,del_product
from Staff.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("accounts/",include("django.contrib.auth.urls")),
    
    #order url link
    path('Order/Create', create_order, name='create_order'), # Create New Order
    path('Order/edit/<int:id>', edit_order, name='edit_order'), # edit Order
    path('Order/Open_Order',Open_order,name='Open_order'),
    path('Order/Close_Order',Close_order,name='Close_order'),
    path('Order/view_Order/<int:id>',view_order,name='view_order'),
    path('Order/print_Order/<int:id>',print_order,name='print_order'),
    path('Order/cancel_Order/<int:id>',cancel_order,name='cancel_order'),
    
    
    
    #product and SHop related link
    path('add_contact', add_shop_detail, name='add_shop_detail'), # update and create shop detail
    path('Product/add_product',add_product,name='add_product'),
    path('Product/list_product',list_product,name='list_product'),
    path('Product/edit_product/<int:id>',edit_product,name='edit_product'),
    path('Product/Delete_product/<int:id>',del_product,name='del_product'),
    
    
    #staff user releated link
    path('staff/create_user_form',Create_staff,name='Create_staff'),
    path('staff/view_staff',view_staff,name='view_staff'),
    path('staff/view_profile/<int:id>', view_profile,name='view_profile'),
    path('staff/edit_profile/<int:id>', edit_staff,name='edit_staff'),
    path('staff/add_salary', add_salary,name='add_salary'),
    path('staff/view_salary/<int:id>', view_salary,name='view_salary'),
    
    #daily expense link
     path('expense/daily_expense', add_daily,name='add_daily'),
     
    
   
    
   
    
    
   
]
