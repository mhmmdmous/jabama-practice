from django.urls import path
from .views import cabin_ticket

urlpatterns = [
    path('cabin-ticket', cabin_ticket)
]