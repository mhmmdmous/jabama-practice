from django.urls import path
from .views import apartment_ticket

urlpatterns = [
    path('hello', apartment_ticket)
]