from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    #path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('find_id/', views.find_id, name='find_id'),
    # path('reset_pw/', auth_views.PasswordResetView.as_view(), name='reset_pw'),
    # path('reset_pw/done', auth_views.PasswordResetDoneView, name='reset_done')

]
