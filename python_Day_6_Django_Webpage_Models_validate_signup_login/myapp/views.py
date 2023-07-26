from django.shortcuts import render,redirect
from .models import Emp

# Create your views here.

def signup(request):
    if request.POST:
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['password']
        obj = Emp(uname=u,email=e,password=p)
        obj.save()
        return redirect("/#")
    return render(request,"signup.html")
def login(request):
    if request.POST:
        e = request.POST['email']
        p = request.POST['password']
        count=Emp.objects.filter(email=e,password=p).count()
        if count>0:
            return redirect("/home")
    return render(request, "login.html")

def home(request):
    return render(request,"home.html")
