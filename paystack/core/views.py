from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,HttpRequest
from . import forms
from django.conf import settings
from django.contrib import messages
from .models import Payment



def initiate_payment(request:HttpRequest)->HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request,'make_payment.html',{"payment":payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()

    return render(request,'initiate_payment.html',{'payment_form':payment_form})
    

def verify_payment(request:HttpRequest,ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment,ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request,"verification succesfull")
    else:
        messages.error(request,"verification failed")

    return redirect('initiate_payment')