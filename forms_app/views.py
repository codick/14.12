from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    return render(request, 'index.html')


def postuser(request):
    name = request.POST.get("name", "Не существует")
    email = request.POST.get("Email", "Не существует")
    phone = request.POST.get("phone", "Не существует")
    service = request.POST.get("service", "Не существует")
    car = request.POST.get("car", "Не существует")
    return HttpResponse(f"<h2> name: {name} email: {email} phone: {phone} service: {service} about: {car} </h2>")


def main(request):
    userform = UserForm()
    if request.method == 'POST':
        name = request.POST.get("name", "Не существует")
        country = request.POST.get('country', 'Не существует')
        town = request.POST.get('town', 'Не существует')
        street = request.POST.get('street', 'Не существует')
        number_house = request.POST.get('number_house', 'Не существует')
        flat = request.POST.get('flat', 'Не существует')
        return redirect('order', name=name, country=country, town=town, street=street, number_house=number_house, flat=flat)
    return render(request, 'main.html', {'form': userform})


def order(request, name, country, town, street, number_house, flat):
    return HttpResponse(f"<h2>{name}, проверьте адрес доставки: <br> {country} <br> {town} <br> {street} <br> {number_house} <br> {flat}")