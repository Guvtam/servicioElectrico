from django.shortcuts import render,redirect
from .forms import ContactoForm
from django.contrib import messages

# Create your views here.
def contacto(request):
   
    if request.method == 'POST':
        form=ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono= form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje=form.cleaned_data['mensaje']
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')
            return redirect('contacto') 
    else:
        form=ContactoForm() 
        return render(request,'contacto/contacto.html',{'form': form})