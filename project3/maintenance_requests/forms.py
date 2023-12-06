from django.forms import *
from django import forms
from .models import *
from .models import add_tenant

class Request_Form(ModelForm):
    class Meta:
        model = Maintenance_Request
        fields = ('issue', 'image')

class Tenant_Form(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'apartment']
    date_check_in = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
    date_check_out = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
    
    def save(self, commit=True):
        return super(Tenant_Form).save(commit=commit)