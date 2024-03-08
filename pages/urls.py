from .views import (
    HomeView,
    AboutView,
    PayView,
    ProductView,
    ContactView,
)
from django.urls import path

urlpatterns = [
    path('contact/', ContactView, name='contact'),
    path('product/', ProductView, name='product'),
    path('pay/', PayView, name='pay'),
    path('about/', AboutView, name='about'),
    path('', HomeView, name='home')
]