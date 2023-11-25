from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    #path('dashboard/', views.dashboard_view, name='dashboard'),
    path('post-create-update/', views.post_create_update, name='post_create_update'),
]