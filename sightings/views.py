from django.shortcuts import render
from map.models import  Squirrel
from django.shortcuts import redirect 
from .forms import SquirrelForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator 

def all(request):
    squirrels = Squirrel.objects.all()
    
    return render(request, 'sightings/all.html',{'squirrels':squirrels})



def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('f/sightings/')
        else:
            form = SquirrelForm()
        return render(request,'sightings/add.html',{'form':form})



def update(request,unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel,unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST,instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/{unique_squirrel_id}')
    else:
        form = squirrelForm(instance = squirrel)
    context = {
        'form': form,
        'unique_squirrel_id':unique_squirrel_id
    }
    return render(request, 'sightings/update.html',context)



def stats(request):
    am_count = 0
    pm_count = 0
    approaches_count = 0
    total = Squirrel.objects.count()
    color = Squirrel.objects.values('primary_fur_color').annotate(Count('primary_fur_color'))
    shift = Squirrel.objects.values('shift').annotate(Count('shift'))
    age= Squirrel.objects.values('age').annotate(Count('age'))
    running = Squirrels.objects.filter(running='TRUE').count()
    for i in Squirrel.objects.all():
        if i.Shift == 'AM':
            am_count += 1
        if i.Shift == 'PM':
            pm_count += 1
        if i.Approaches == True:
        approaches_count += 1

    context = {
        'AM_Count': am_count,
        'PM_Count': pm_count,
        'Approaches_Count': approaches_count,
        'total':total,
        'color':color,
        'shift':shift,
        'age':age,
        'running':running
    }
    
    return render(request, 'sightings/stats.html',context)


# Create your views here.
