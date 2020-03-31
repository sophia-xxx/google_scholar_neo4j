from rest_framework import generics

from .models import Author
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    #print("result: " + str(queryset))
    serializer_class = TodoSerializer
