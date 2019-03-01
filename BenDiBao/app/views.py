from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from app.models import Activity
def index(request):

    acts = Activity.objects.all();

    # for var in acts:
        
    return HttpResponse('Hello World !')