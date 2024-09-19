from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        c1 = Data(name=name, pno=pno, email=email, un=un, pw=pw)
        c1.save()
        return HttpResponse('Done.....:)')
    return render(request, 'register.html')