from . import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,name='mainpage.html'),
    path('customerlist/',views.customerlist,name='customerlist'),
    path('transfermoney/',views.transfer,name='transfer'),
    path('send_money/',views.send_money,name='send_money'),
]
