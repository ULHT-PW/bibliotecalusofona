from django import forms
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'

    widgets = {
      'autor': forms.TextInput(attrs={
          'placeholder':'Nome completo',
      })
    }    

class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    fields = '__all__'