from django.urls import path
from .views import apartment_ticket

urlpatterns = [
    path('apartment-ticket', apartment_ticket)
]