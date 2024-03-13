from rest_framework import status
from rest_framework.views import APIView
from .models import Student, Teacher
from .serializer import StudentSerializer, TeacherSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterStudent(APIView):
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = Student.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({'status': 200, 'payload': serializer.data,'refresh':str(refresh), 'accesss': str(refresh.access_token),
                             'message': 'New user has been registered'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RegisterTeacher(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = Teacher.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({'status': 200, 'payload': serializer.data,'refresh':str(refresh), 'accesss': str(refresh.access_token),
                             'message': 'New user has been registered'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
from django.contrib.auth import authenticate

class LoginStudent(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user and isinstance(user, Student):
            # Generate JWT tokens
            return Response({'status': 200, 'access': "Successfully loggedin"})

        return Response({'status': 401, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LoginTeacher(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user and isinstance(user, Teacher):
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({'status': 200, 'access': str(refresh.access_token), 'refresh': str(refresh)})

        return Response({'status': 401, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

                