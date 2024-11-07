from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Ordem
from .forms import OrderForm
from .utils import send_telegram_notification

# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            Ordem = form.save()
            message = (
                f"Novo Pedido de {Ordem.nome}\n"
                f"Endereço: {Ordem.endereco}\n"
                f"Itens: {Ordem.items}"
            )
            send_telegram_notification(message)
            return redirect("order_success")
    else:
        form = OrderForm()
    return render(request, "delivery/create_order.html", {"form": form})

def order_success(request):
    return HttpResponse("Pedido enviado com sucesso!")
