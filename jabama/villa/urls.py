from django.urls import path
from .views import villa_ticket

urlpatterns = [
    path('villa-ticket', villa_ticket)
]