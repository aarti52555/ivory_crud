from django.urls import path

from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
)

app_name = "user"
urlpatterns = [
    path('', UserListView.as_view(), name='user_views'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
