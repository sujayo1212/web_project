import null as null
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponseForbidden, HttpResponseRedirect
from common.models import CustomUser as User
from lecture.models import Lecture
from .forms import CustomUserChangeForm, PasswordCheckForm



# # Create your views here.

#마이페이지
def my_page(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = request.user.first_name
        last_name = request.user.last_name
        full_name = first_name+last_name
        lectures = Lecture.objects.filter(member=user)

        context = {
            'username': user,
            'first_name': first_name,
            'last_name': last_name,
            'full_name': full_name,
            'lectures': lectures,

        }

        return render(request, 'my_page/my_page.html', context)
    else:
        return redirect('/common/login')


#정보수정페이지
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        context= {'form': form}
    return render(request, 'my_page/update.html', context)




#나의수강정보
def my_lecture(request):
    user = request.user
    lectures = Lecture.objects.filter(member=user)
    return render(request, 'my_page/my_lecture.html', {'lectures': lectures})


#수강신청
@login_required
def join_lecture(request, id):
    user = request.user
    lecture = Lecture.objects.get(pk=id)

    if lecture.member.count() >= lecture.max_member:
        return render(request, 'my_page/max.html')

    else:
        lecture.member.add(user)
        lecture.save()
    return render(request, 'my_page/join_lecture.html')

#수강취소
# @login_required
# def cancel_lecture(request, id):
#     user =request.user
#     lecture = Lecture.objects.get(pk=id)
#     lecture.member.remove(user)
#     return render(request, )




#회원탈퇴
def delete(request):
    if request.method == 'POST':
        form = PasswordCheckForm(request.user, request.POST)
        if form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('home')
    else:
        messages.error("비밀번호가 틀립니다.")
        form = PasswordCheckForm(request.user)

    return render(request, 'my_page/delete.html', {'form': form})

