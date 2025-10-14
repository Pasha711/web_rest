from django.urls import path
from .views import UserRegisterView, UserProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'), #GET, PUT, DELETE
]
