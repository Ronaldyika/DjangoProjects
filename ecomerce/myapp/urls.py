from django.urls import path
from . import views
from .views import ValidateUserView
from django.views.decorators.csrf import csrf_exempt
 
urlpatterns = [
    path('',views.home,name='homepage'),
    path('add-expense',views.add_expense,name='add-expense'),
    path('register/',views.register,name='register'),
    path('validate_username/',csrf_exempt(ValidateUserView.as_view()),name='validate_user')

]