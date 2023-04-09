from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from knox.auth import TokenAuthentication

def get_token(user):
    token = AuthToken.objects.create(user)
    return token[1]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_token(user)
            return Response({"token": token}, status=status.HTTP_201_CREATED)
        
        if "duplicate" in serializer.errors:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = get_token(user)
            
            return Response({"token": token}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)