from django.db import models

class Ordem(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    items = models.TextField()  # Itens do pedido, por exemplo: "Pizza, Refrigerante"
    data_e_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.nome}"
