from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
def index(req):
    if req.user.username:
        username = req.user.first_name
        # print(req.user.first_name, '#', req.user.id)
    else:
        username = 'Гость'
        print(req.user.id)
        # username = req.user.username
    data = {'username': username}
    # user = User.objects.create_user('user2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()
    return render(req, 'index.html', context=data)





from .form import SignUpform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def registr(req):
    if req.POST:
        anketa = SignUpform(req.POST)
        if anketa.is_valid():
            print('ok')
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user=authenticate(username=k1,password=k2)  #сщздает пользователя регистрирует
            man = User.objects.get(username=k1)           #найдем нового пользователя.
            #заполним поля в таблице
            man.email=k5
            man.first_name=k3
            man.last_name = k4
            man.save()
            login(req,user)                              #входит на сайт новым пользователем
                                
            return redirect('home')
    else:
        anketa = SignUpform()
    data={'regform':anketa}
    return render(req,'registration/registration.html',context=data)