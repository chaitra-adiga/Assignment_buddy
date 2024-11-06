from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginn, name='loginn'),
    path('logout/', views.logoutt, name='logoutt'),
    path('register/', views.register_user, name='register_user'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]
