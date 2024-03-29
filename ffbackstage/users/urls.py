from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.LoginUser.as_view(), name='login'),
]
