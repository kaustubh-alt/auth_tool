from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.register,name="register"),
    path('login/', views.custom_login_view,name="login"),
    path('logout_user/',views.logout,name="logout"), 
    path('home/', views.home,name="home"),
    path('forgot_password/', views.forgotpassword,name="forgot_password"),
    path('activate/<str:id>/', views.activate,name="forgot_password"),
     
]