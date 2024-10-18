from django.urls import path
from . import views

app_name = 'manejadorpagosApp'

urlpatterns = [
    #path('recibos/', views.ReciboListView.as_view(), name='recibo_list'),
    path('recibos/<int:receipt_number>/', views.get_recibo, name='get_recibo'),
]