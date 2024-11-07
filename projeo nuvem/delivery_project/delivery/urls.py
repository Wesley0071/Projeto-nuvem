from django.urls import path
from . import views

urlpatterns = [
    path("pedido/", views.create_order, name="create_order"),
    path("sucesso/", views.order_success, name="order_success"),

]
