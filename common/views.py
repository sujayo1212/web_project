from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from typing import Any, Dict
from .forms import UserForm, StaffForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def signup(request):
    if request.method == 'POST':  # request 들어온 것이 post방식이면
        if request.POST['teacher_code'] in ['A0001', 'A0002']:
            form = StaffForm(request.POST)
        else:
            form = UserForm(request.POST)  # form에 UserForm post version으로 저장한다
        if form.is_valid():  # form이 valid하면
            form.save()
            return redirect('../login')
    else:
        form = UserForm()  # 계정 생성 화면 리턴
    return render(request, './common/signup.html', {'form': form})


def find_id(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            context = {'username': user.username}
            return render(request, './common/find_id.html', context)
        except ObjectDoesNotExist:
            context = {'username': "None"}
            return render(request, './common/find_id.html', context)

    else:
        return render(request, './common/find_id.html')

#
# class PasswordResetView(PasswordResetView):
#     template_name = './common/password_reset.html'
#