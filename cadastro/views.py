from django.shortcuts import render, redirect
from .forms import CadastroClienteForm

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhes_cliente', cliente_id=form.instance.id)
    else:
        form = CadastroClienteForm()

    return render(request, 'cadastro_cliente/cadastrar_cliente.html', {'form': form})
