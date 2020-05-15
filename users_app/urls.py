from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # path('', views.home, name='home'),

    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')


    # path('delete/<task_id>', views.delete_task, name='delete_task'),
    # path('edit/<task_id>', views.edit_task, name='edit_task'),
    # path('complete/<task_id>', views.complete_task, name='complete_task'),


]
