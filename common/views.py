from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from typing import Any, Dict
from .forms import UserForm, StaffForm
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def signup(request):
    if request.method == 'POST':#request 들어온 것이 post방식이면
        if request.POST['teacher_code'] in ['A0001', 'A0002']:
            form = StaffForm(request.POST)
        else:
            form = UserForm(request.POST)#form에 UserForm post version으로 저장한다
        if form.is_valid(): # form이 valid하면
            form.save()
            return redirect('../login')
    else:
        form = UserForm() # 계정 생성 화면 리턴
    return render(request, './common/signup.html', {'form': form})


