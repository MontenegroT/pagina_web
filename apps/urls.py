from django.urls import path
from apps.views import inicio, libroslist, BookDetailView, acerca_de_mi, LibForm

urlpatterns = [
    path('',inicio, name='Inicio'),
    path('biblioteca/', libroslist.as_view(), name='Biblioteca'),
    path('libros/<int:pk>/', BookDetailView.as_view(), name='detalles'),
    path('acerca_de_mi/', acerca_de_mi, name='Acercademi'),
    path('libform/', LibForm, name='libform')

]

#r'^(?P<pk>\d+)$'