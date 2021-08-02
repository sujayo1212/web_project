from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm

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
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        context={'form': form}
    return render(request, 'my_page/update.html', context)

        # user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        # if user_change_form.is_valid():
        #     user_change_form.save()
        #     return render(request, 'home.html')
    #
    # else:
    #     user_change_form = CustomUserChangeForm(instance=request.user)
    #     return render(request, 'my_page/update.html', {'user_change_form': user_change_form})

def my_lecture(request):
    user = request.user

    return render(request, 'my_page/my_lecture.html')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()

    return redirect('home')