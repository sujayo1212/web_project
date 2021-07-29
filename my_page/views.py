from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

def mypage(request):
    if request.user.is_authenticated:
        context={
            'username':request.user
        }
        return render(request, 'my_page/my_page.html', context)

