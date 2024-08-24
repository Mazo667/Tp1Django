from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='mensajes/home.html'),name='home'),
    path('recibidos/', TemplateView.as_view(template_name='mensajes/recibidos.html'),name='recibidos')
]