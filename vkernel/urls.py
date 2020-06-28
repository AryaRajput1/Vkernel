from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('mainpage/',views.mainpage),
    path('login/',views.loginpage),
    path('signup/',views.signuppage),
    path('logout/',views.logoutpage),
    path('account/',views.account),
    path('subscribe/',views.Buypage),
    path('videoc/<int:id>/',views.videostopic),
    path('videocontent/<int:id>/',views.videocontent),
    path('PaymentPage/<int:id>/',views.Payment),
    path('handlerequest/',views.handlerequest),
]