from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Order, Customer


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address", "mobile", "email"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address" ]
    def clean_username(self):
        uname=self.cleaned_data.get('username')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("khay wezon lyhfdak bdal had smia rah deja kyna wla ktab smitk ozid liha chy hraf")
        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)