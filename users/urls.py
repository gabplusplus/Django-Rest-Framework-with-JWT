from django.urls import path
from .views import CustomUserCreate, UserLoginView, test

app_name = 'users'

urlpatterns = [
    # Creation of account
    path('create/', CustomUserCreate.as_view(), name='create_user'),
    # Logging in to the server
    path('login/', UserLoginView.as_view(), name='login'),
    path('test/', test, name='test')
]