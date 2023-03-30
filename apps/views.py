from django.shortcuts import render
from .models import libros
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from apps.form import libforms
# Create your views here.

def inicio(request):
    return render(request, 'apps/inicio.html')

def acerca_de_mi(request):
    return render(request, 'apps/acercademi.html')

class libroslist(ListView):
    model=libros
    template_name="apps/biblioteca.html"

class BookDetailView(DetailView):
    model = libros
    template_name = 'apps/libros_detalles.html'
    context_object_name = 'libros'


def LibForm(request):
    if request.method == "POST":
        miform=libforms(request.POST)
        print(miform)
        if miform.is_valid:
            info=miform.cleaned_data
            libs=libros(titulo=info['titulo'], genero=info['genero'], pagina=info['paginas'], autor=info['autor'])
            libs.save()
            return render(request, 'apps/inicio.html')
        else:
            miform=libforms()

    return render(request, "apps/libform.html", {'miform': miform})





 
 
