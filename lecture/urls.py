from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('', views.LectureList.as_view(), name='index'),
    path('<int:pk>/', views.LectureDetail.as_view(), name='detail'),
    path('create/', views.lecture_create, name='lecture_create'),
    path('<int:lecture_id>/update/', views.lecture_update, name='lecture_update'),
    path('<int:lecture_id>/delete/', views.lecture_delete, name='lecture_delete'),
]