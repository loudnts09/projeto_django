from django.shortcuts import render, redirect
from .forms import PizzaForm

def cadastrar_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhes_pizza', pizza_id=form.instance.id)
    else:
        form = PizzaForm()

    return render(request, 'pizzas/cadastrar_pizza.html', {'form': form})
