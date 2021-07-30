from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView


def my_page(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = request.user.first_name
        last_name = request.user.last_name
        context = {
            'username': user,
            'first_name': first_name,
            'last_name': last_name
        }
        return render(request, 'my_page/my_page.html', context)
    else:
        return redirect('/common/login')

