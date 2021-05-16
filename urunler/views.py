from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import urun

# Create your views here.

def index(request):
    urunler = urun.objects.all()
    context = {
        'urunler' : urunler
    }
    return render(request,'urunler/list.html', context)

def detail(request, urun_id):
    urunler = get_object_or_404(urun, pk = urun_id)
    context = {
        'urunler' : urunler
    }
    return render(request,'urunler/detail.html', context)

def search(request):
    return render(request,'urunler/search.html')