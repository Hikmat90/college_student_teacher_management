from .serializers import ContentSerializer
from .models import content
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user.models import Student,Teacher
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ContentCRUD(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the user is a Student instance
            if isinstance(request.user, Student):
                serializer.save(created_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is not None:
            instance = get_object_or_404(content, pk=pk)
            serializer = ContentSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            query = content.objects.all()
            serializer = ContentSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            query = get_object_or_404(content, pk=pk)
            serializer = ContentSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        if pk is not None:
            instance = get_object_or_404(content, pk=pk)
            serializer = ContentSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = get_object_or_404(content, pk=pk)
        query.delete()
        return Response({'message': 'Content deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class TeacherView(APIView):
    def get(self, request,pk=None):
        if pk is not None:
            instance = get_object_or_404(content, pk = pk)
            if isinstance(request.user,Teacher):
                serializer = ContentSerializer(instance,many = True)
                return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            instance = content.objects.all()
            if isinstance(request.user,Teacher):
                serializer = ContentSerializer(instance)
                return Response(serializer.data,status = status.HTTP_202_ACCEPTED)