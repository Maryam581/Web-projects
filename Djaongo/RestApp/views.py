from django.shortcuts import render 
from django.http import HttpResponse
def RestTest(request): 
 return HttpResponse("<h2> Hello RestApp</h2>") 

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
