from django import forms

class libforms(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    genero=forms.CharField()
    paginas=forms.IntegerField()