from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserForm(UserCreationForm):
    last_name = forms.CharField(label="성")
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")
    teacher_code = forms.CharField(label='강사코드')

    class Meta:
        model = User
        fields = (
            "username",
            "last_name",
            "first_name",
            "password1",
            "password2",
            "email"
        )

    def save(self):
        user = super(UserForm, self).save(commit=False)
        user.save()
        try:
            student = Group.objects.get(name='student')
            student.user_set.add(user)
        except Group.DoesNotExist:
            student = Group.objects.create(name='student')
            student.user_set.add(user)
        return

    # 보통 meta 클래스는 field로 정의 할 수 없는 것들을 정의하기 위해 사용한다는 것인데
    # 순서(order)나 단수 복수형 추가(안하면 뒤에 s만 붙음)
    # wikidocs에서 왜 이렇게 쓴느지는 잘 모르겠음


class StaffForm(UserCreationForm):
    last_name = forms.CharField(label="성")
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")
    teacher_code = forms.CharField(label='강사코드')

    class Meta:
        model = User
        fields = (
            "username",
            "last_name",
            "first_name",
            "password1",
            "password2",
            "email"
        )

    def save(self):
        user = super(StaffForm, self).save(commit=False)
        user.is_staff = True
        user.save()
        try:
            teacher = Group.objects.get(name='teacher')
            teacher.user_set.add(user)
        except Group.DoesNotExist:
            teacher = Group.objects.create(name='teacher')
            teacher.user_set.add(user)
        return





