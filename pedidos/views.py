# pedidos/views.py
from django.shortcuts import render, redirect
from .forms import PedidoForm

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhes_pedido', pedido_id=form.instance.id)
    else:
        form = PedidoForm()

    return render(request, 'pedidos/cadastrar_pedido.html', {'form': form})
