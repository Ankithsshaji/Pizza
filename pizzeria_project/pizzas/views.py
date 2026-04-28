from django.shortcuts import render

# Create your views here.
from .models import Pizza

def index(request):
    return render(request, 'pizzas/pizzas.html')

def pizza(request, pizza_id):
    """Show a single pizza and its toppings."""

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {
        'pizza': pizza,
        'toppings': toppings
    }

    return render(request, 'pizzas/pizza.html', context)

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)