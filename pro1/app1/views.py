from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContentForm
from .models import Content

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

def formview(request):
    form = ContentForm()
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def showview(request):
    obj = Content.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Content.objects.get(cid = pk)
    form = ContentForm(instance=obj)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def deleteview(request, x):
    obj = Content.objects.get(cid = x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv')
    return render(request, 'app1/success.html', {'obj': obj})