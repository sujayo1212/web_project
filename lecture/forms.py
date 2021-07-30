from django import forms
from .models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['class_name', 'subject', 'detail_subject', 'content', 'price', 'lecture_image']
        labels = {
            'class_name': '강의명',
            'subject': '과목',
            'detail_subject': '세부과목',
            'content': '내용',
            'price': '가격',
            'lecture_image': '이미지'
        }

