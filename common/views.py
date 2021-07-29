from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserForm, StaffForm
# Create your views here.


def signup(request):
    if request.method == 'POST':#request 들어온 것이 post방식이면
        if request.POST['teacher_code'] in ['A0001', 'A0002']:
            form = StaffForm(request.POST)
        else:
            form = UserForm(request.POST)#form에 UserForm post version으로 저장한다
        if form.is_valid(): # form이 valid하면
            form.save()
            return redirect('/common/login')
    else:
        form = UserForm() # 계정 생성 화면 리턴
    return render(request, 'common/signup.html', {'form': form})


def main(request):
    return render(request, 'common/main.html')