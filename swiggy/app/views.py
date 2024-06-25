from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import *

# Create your views here.
def first(request):
    list=['a','b','c',['a','z']]
    return render(request,"first.html",context={"l":list})
#context only accept values in form of dict.

def second(request):
    if request.method=='POST':
        d=request.POST
        name=d.get("name")
        age=d.get("age")
        gender=d.get("gender")
        print(name)
        print(age)
        print(gender)
        z=A(name=name,age=age,gender=gender)
        z.save()
    k=A.objects.all()
    return render(request,"second.html",context={"value":k})

def delete(request,id):
    c=A.objects.get(id=id)
    c.delete()
    return redirect("/")

def update(request,id):
    k=A.objects.get(id=id)
    if request.method=='POST':
        d=request.POST
        a=d.get("name")
        b=d.get("age")
        c=d.get("gender")

        k.name=a
        k.age=b
        k.gender=c
        k.save()
        return redirect("/")
    return render(request,"update.html")
    

