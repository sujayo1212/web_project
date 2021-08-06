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
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]