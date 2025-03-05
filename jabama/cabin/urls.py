from django.urls import path
from .views import cabin_ticket

urlpatterns = [
    path('hello', cabin_ticket)
]