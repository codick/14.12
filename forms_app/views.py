from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def postuser(request):
    name = request.POST.get("Name", "Не существует")
    Email = request.POST.get("Email", "Не существует")
    phone = request.POST.get("Phone Number", "Не существует")
    service = request.POST.get("Select Service", "Не существует")
    car = request.POST.get("about", "Не существует")
    return HttpResponse(f"<h2> name: {name} email: {Email} phone: {phone} service: {service} about: {car} </h2>")