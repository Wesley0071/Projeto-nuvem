from django.contrib import admin
from  delivery import views
from django.urls import path, include

urlpatterns = [
    path('', views.create_order, name='OS'),
    path("", include("delivery.urls")),
]
