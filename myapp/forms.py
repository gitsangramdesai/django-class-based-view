
from django import forms
from .models import  SiteUser

class SiteUserForm(forms.ModelForm):
    options = (
        ('active', 'Active'),
        ('inactive', 'InActive'),
    )
    
    country_option = (
        (1, 'India'),
        (2, 'Pakistan'),
        (3, 'Bangladesh'),
        (4, 'Nepal'),
        (5, 'Bhutan'),
        (6, 'China'),
    )
    
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="First Name")
    lastName = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Last Name")
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Email")
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}),label="Birth Date")
       
    addressLine1 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows':'3'}),label="Address Line 1")
    addressLine2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows':'3'}),label="Address Line 2")
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="State")
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="City")
    pin = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Pin")
    status = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}),label="Status")
    country = forms.IntegerField(widget=forms.Select(choices=country_option, attrs={'class': 'form-control'}),label="Country")
    
    class Meta:
        model = SiteUser
        fields = ['firstName', 'lastName', 'email','dob', 'addressLine1', 'addressLine2', 'state','city','pin','status','country']
