from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}))
    last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}))
    email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}))
    phone = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}))
    address = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}))
    city = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}))
    state = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}))
    zipcode = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","class":"form-control"}))
    
    class Meta:
        model = Record
        fields =['first_name','last_name','email','phone','address','city','state','zipcode']
    