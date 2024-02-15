from django import forms
from .models import Cliente, Endereco

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'celular', 'email', 'senha']

    rua = forms.CharField()
    numero = forms.IntegerField()
    bairro = forms.CharField()

    def save(self, commit=True):
        endereco = Endereco.objects.create(
            rua=self.cleaned_data['rua'],
            numero=self.cleaned_data['numero'],
            bairro=self.cleaned_data['bairro']
        )
        self.cleaned_data['endereco'] = endereco
        return super().save(commit)
