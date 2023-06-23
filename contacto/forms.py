from django import forms 
from .models import FormularioContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=FormularioContacto
        fields=['nombre','email', 'telefono', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email*'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','placeholder':'Teléfono*'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,'placeholder':'Mensaje*'}),
        }
        