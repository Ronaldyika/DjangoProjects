from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

def home(request):
    return render(request,'index.html')

def add_expense(request):
    return render(request,'expense/add_expense.html')

class ValidateUserView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']

        if str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'})
        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_exist': 'username already exists'},status = 409)
        return JsonResponse({'username_valid': True})


def register(request):
    return render(request,'base_auth/base_auth.html')