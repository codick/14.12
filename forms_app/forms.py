from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    town = forms.CharField()
    street = forms.CharField()
    number_house = forms.IntegerField()
    flat = forms.IntegerField()
