from django.urls import path
from .views import CustomUserCreate, UserLoginView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
    path('login/', UserLoginView.as_view(), name='login')
]