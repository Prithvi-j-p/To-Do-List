from django.contrib import admin
from django.urls import path
from one import views


urlpatterns = [
    path('one', views.one),
    path('two', views.two),
    path('three', views.three),
    path('four', views.four),
    path('weekone',views.weekone),
    path('weekoneinsert',views.weekoneinsert),
    path('weektwo',views.weektwo),
    path('weektwoinsert',views.weektwoinsert),
    path('weekthree',views.weekthree),
    path('weekthreeinsert',views.weekthreeinsert),
    path('weekfour',views.weekfour),
    path('weekfourinsert',views.weekfourinsert),
    path('allrows',views.allrows),
    path('deleteweekonedata',views.deleteweekonedata),
    path('deleteweekone',views.deleteweekone),
    path('cookie', views.cookie),
    path('set_cookies',views.set_cookie),
    path('get_cookies',views.one),
    path('deletecookie',views.delete_cookie),
    path('cookie2',views.cookie2),
    path('loginpage',views.loginpage),
    path('register',views.register),
    path('registerpage',views.registerpage),
    path('login',views.login),
]