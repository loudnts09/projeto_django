from django import forms
from .models import Bordas, Massas, Pizza, Sabores

class PizzaForm(forms.ModelForm):
    sabor = forms.ModelMultipleChoiceField(queryset=Sabores.objects.all())
    
    class Meta:
        model = Pizza
        fields = ['bordas', 'massa']
