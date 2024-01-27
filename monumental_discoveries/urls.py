from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('services',views.service, name='services'),
    path('booking-service/<str:name>',views.booking_service, name='booking_service'),
]


