from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    path('', views.index, name='index'),
    # 127.0.0.1:8000/qna 가 디폴트
    path('<int:question_id>/', views.detail, name='detail'),
    # 127.0.0.1:8000/qna/ + int값이 들어옴 -> question_id
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # 127.0.0.1:8000/qna/answer/creat/number$$$
    path('question/create/', views.question_create, name='question_create'),
    # 127.0.0.1:8000/qna/question/create/
]
