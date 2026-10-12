from django import forms
from django.forms import ModelForm
from .models import Product


# class InsertForm(forms.Form):
#  title = forms.CharField()
#  description = forms.CharField()
class InsertForm(forms.Form):
 product_name=forms.CharField(max_length=200,
widget=forms.TextInput(attrs={'class':'form-control','name':'p_name'}))
 product_company=forms.CharField(max_length=200,
 widget=forms.TextInput(attrs={'class':'form-control','name':'p_company'}))
 product_price=forms.CharField(max_length=200,
widget=forms.TextInput(attrs={'class':'form-control','name':'p_price'}))
 
class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = '__all__'

 
