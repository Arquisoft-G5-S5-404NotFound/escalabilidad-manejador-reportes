from django.shortcuts import render
from django.http import JsonResponse
from .models import Recibo
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
u=authenticate(username="john", password="johnpassword")#User.objects.create_user(username="john", password="johnpassword", email="jd.sanchez2@uniandes.edu.co", first_name="John", last_name="Doe")
#Recibo.objects.create(user=u, amount=100, transaction_id='1', receipt_number='1', status='completed', description='Pago de prueba', payment_method='credit_card')

def get_recibo(request, receipt_number):
    recibo=Recibo.objects.get(receipt_number=receipt_number)
    return JsonResponse({'receipt_number': recibo.receipt_number, 'amount': recibo.amount, 'payment_date': recibo.payment_date, 'transaction_id': recibo.transaction_id, 'status': recibo.status, 'description': recibo.description, 'payment_method': recibo.payment_method})