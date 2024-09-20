from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('users/reg/', views.RegistrationAPIView.as_view()),
    path('users/login/', views.LoginAPIView.as_view()),
    path('user', views.UserRetrieveUpdateAPIView.as_view()),
]