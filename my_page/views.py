from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

#
# # Create your views here.


def my_page(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = request.user.first_name
        last_name = request.user.last_name
        full_name = first_name+last_name
        context = {
            'username': user,
            'first_name': first_name,
            'last_name': last_name,
            'full_name': full_name,
        }
        return render(request, 'my_page/my_page.html', context)
    else:
        return redirect('/common/login')

@login_required
def update(request):
    # if request.method == 'POST':
    #     user = request.user
    #     email = request.POST.get('email')
    #
    #     user.email = email
    #     user.save()
        return render(request, 'my_page/update.html')