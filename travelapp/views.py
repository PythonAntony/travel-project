from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import features
# Create your views here.
# def displaymessage(request):
#     return HttpResponse("<h1 style='text-align:center;'>Hello World</h1>")
def home(request):
    obj=place.objects.all()
    obj1=features.objects.all()
    return render(request, "index.html",{'result':obj, 'result1':obj1})