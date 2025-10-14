from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegisterSerializer, UserProfileSerializer
from .models import CustomUser
import logging


logger = logging.getLogger(__name__)

class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f"Новий користувач зареєстрован: {user.email}")
            return Response({'message': 'Користувача успішно створено!'}, status=status.HTTP_201_CREATED)
        logger.warning(f"Помилка реєстрації. Дані: {request.data}. Помилки: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        logger.info(f"Користувач {user.email} запросив свій профіль.")
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Користувач {user.email} оновив свій профіль.")
            return Response(serializer.data)
        logger.warning(f"Помилка оновлення профіля для {user.email}. Помилки: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user_email = user.email
        user.delete()
        logger.info(f"Користувач {user_email} видалив свій акаунт.")
        return Response({'message': 'Акаунт успішно видалено.'}, status=status.HTTP_204_NO_CONTENT)
    