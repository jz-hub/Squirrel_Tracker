from django.shortcuts import render 
from .models import Squirrel


def index(request):
    squirrels_map = Squirrel.objects.all()[:80]
    context = {
        'squirrels_map': squirrels_map,
    }
    return render(request ,'map/index.html',context)

#Create your views here
