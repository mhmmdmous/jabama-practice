from django.urls import path
from .views import villa_ticket

urlpatterns = [
    path('hello', villa_ticket)
]