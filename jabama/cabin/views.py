from django.http.response import HttpResponse

# Create your views here.
def cabin_ticket(request):
    return HttpResponse("Hey! This is cabin page")