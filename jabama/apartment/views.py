from django.http.response import HttpResponse

# Create your views here.
def apartment_ticket(request):
    return HttpResponse("Hey! This is apartment page")