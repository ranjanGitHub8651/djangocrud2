from django.shortcuts import render, HttpResponseRedirect
from .models import Student

def HomePage(request):
    data = Student.objects.all()
    return render(request, "index.html", {"data":data})

def AddNew(request):
    if(request.method == "POST"):
        dt = Student()
        dt.name = request.POST.get("name")
        dt.email = request.POST.get("email")
        dt.number = request.POST.get("number")
        dt.city = request.POST.get("city")
        dt.save()
        return HttpResponseRedirect("/")
    return render(request, "add.html")

def UpdateRcd(request, id):
    dt = Student.objects.get(id=id)
    if(request.method=="POST"):
        dt.name = request.POST.get("name")
        dt.email = request.POST.get("email")
        dt.number = request.POST.get("number")
        dt.city = request.POST.get("city")
        dt.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {"dt":dt})

def DeleteRcd(request, id):
    dt = Student.objects.get(id=id)
    dt.delete()
    return HttpResponseRedirect("/")










