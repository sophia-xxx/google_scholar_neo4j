#from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Author
from .serializers import AuthorSerializer

@api_view(('GET',))
def AllAuthors(req):
    authors = Author.objects.raw('SELECT name, affiliation FROM Authors')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)
@api_view(('GET',))
def AuthorById(req, ID):
    author = Author.objects.raw('SELECT id, name, affiliation FROM Authors WHERE id = %s', [ID])
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)


# class AllAuthors(generics.ListCreateAPIView):
#     authors = Author.objects.raw('SELECT id, name, affiliation FROM Authors')
#     serializer_class = AuthorSerializer
#
#
# class AuthorById(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     #print("result: " + str(queryset))
#     serializer_class = AuthorSerializer
