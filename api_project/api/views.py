from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#iTask2: creating viewset
from rest_framework import viewsets  #additional imports in addition to the initials above
#creat your views here
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#make sure to register the viewset in urls


#Task3: generate and use tokens as authorization/permission to authenticate requests
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
#create your views here
class AuthenticatedViewSet(viewsets.ModelViewSet):
    '''permits view for only authenticated user'''
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AdminViewSet(viewsets.ModelViewSet):
    '''allows views for only admin user'''
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PublicView(APIView):
    '''allows anyone to view'''
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a public endpoint."})



