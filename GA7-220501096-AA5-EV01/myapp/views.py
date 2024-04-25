from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .serializers import UserSerializer

class RegisterAPI(APIView):
    """
    Endpoint para registro de usuarios.
    """
    def post(self, request):
        # Serializar los datos de la solicitud
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Crear un nuevo usuario
            serializer.save()
            return Response({"message": "Registro exitoso"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    """
    Endpoint para inicio de sesión.
    """
    def post(self, request):
        # Serializar los datos de la solicitud
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # Autenticar al usuario
            user = authenticate(username=username, password=password)
            if user:
                return Response({"message": "Autenticación satisfactoria"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Error en la autenticación"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
