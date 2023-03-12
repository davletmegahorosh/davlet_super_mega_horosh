from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserValidateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from rest_framework.views import APIView

class RegistrationAPIView(APIView):
    def registration_view(self,request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user =User.objects.create_user(username= serializer.validated_data('username'),
                                 password= serializer.validated_data('password'),
                                 is_active=False)
        confirmcode = random.randint(100000, 999999)
        user.confirmcode  =confirmcode
        user.save()
        return Response({'confirmcode' : confirmcode},status=status.HTTP_201_CREATED)

class ConfirmAPIView(APIView):
    def confirm_view(self,request):
        username = request.data.get('username')
        confirmcode = request.data.get('confirmcode')
        try:
            user = User.objects.get(username=username, confirmcode=confirmcode)
        except User.DoesNotExist:
            return Response({'error':'Invalid username or confirm code'}, status = status.HTTP_404_NOT_FOUND)
        user.is_active = True
        user.confirmcode = None
        user.save()
        return Response({'message' : 'user registrated succesesfully'}, status=status.HTTP_200_OK)

class AuthorizationAPIView(APIView):

    def authorization_view(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username = serializer.validated_data.get('username'),
                            password = serializer.validated_data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)