from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place, place1, place2, place3, place4


# Create your views here.
def home(request):
    obj1 = place.objects.all()
    obj2 = place1.objects.all()
    obj3 = place2.objects.all()
    obj4 = place3.objects.all()
    obj5 = place4.objects.all()

    return render(request, "index.html",
                  {'result': obj1, 'result1': obj2, 'result2': obj3, 'result3': obj4, 'result4': obj5})
