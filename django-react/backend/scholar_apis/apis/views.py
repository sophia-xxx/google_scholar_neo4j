#from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer
from django.db import connection

#views for fetching authors
@api_view(('GET',))
def AllAuthors(req):
    authors = Author.objects.raw('SELECT * FROM Authors')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def AuthorsById(req, ID):
    author = Author.objects.raw('SELECT * FROM Authors WHERE id = %s', [ID])
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def AuthorsByName(req, name):
    name = name.replace('+', ' ').lower()
    authors = Author.objects.raw('SELECT * FROM Authors WHERE LOWER(name) = %s', [name])
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def AuthorsByNameAffiliation(req, name, affiliation):
    name = name.replace('+', ' ').lower()
    affiliation = affiliation.replace('+', ' ').lower()
    author = Author.objects.raw('SELECT * FROM Authors WHERE LOWER(name) = %s AND LOWER(affiliation) = %s', [name, affiliation])
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)

# views for fetching articles
@api_view(('GET',))
def AllArticles(req):
    articles = Article.objects.raw('SELECT * FROM Articles')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def ArticlesById(req, ID):
    articles = Article.objects.raw('SELECT * FROM Articles WHERE id = %s', [ID])
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def ArticlesByName(req, name):
    name = name.replace('+', ' ').lower()
    articles = Article.objects.raw('SELECT * FROM Articles WHERE LOWER(name) = %s', [name])
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def ArticlesByNameAffiliation(req, name, affiliation):
    name = name.replace('+', ' ').lower()
    affiliation = affiliation.replace('+', ' ').lower()
    articles = Article.objects.raw('SELECT * FROM Articles WHERE LOWER(name) = %s AND LOWER(affiliation) = %s', [name, affiliation])
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def ArticlesByJournal(req, journal):
    journal = journal.replace('+', ' ').lower()
    articles = Article.objects.raw('SELECT * FROM Articles WHERE LOWER(journal) = %s', [journal])
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

#create author, article
@api_view(('POST',))
def AddAuthor(req):
    serializer = AuthorSerializer(data=req.data)
    if(serializer.is_valid()):
        with connection.cursor() as cursor:
            name = serializer.data['name'].lower()
            affiliation = serializer.data['affiliation']
            name = name.replace('+', ' ')
            affiliation = affiliation.replace('+', ' ')
            cursor.execute("INSERT INTO AUTHORS(name, affiliation) VALUES (%s, %s )", [name, affiliation])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('POST',))
def AddArticle(req):
    serializer = ArticleSerializer(data=req.data)
    if(serializer.is_valid()):
        with connection.cursor() as cursor:
            sql, values = create_article_sql(serializer.data)
            cursor.execute(sql, values)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update article
@api_view(('PUT',))
def UpdateArticle(req):
    serializer = ArticleSerializer(data=req.data)
    if(serializer.is_valid()):
        with connection.cursor() as cursor:
            sql, values = update_article_sql(serializer.data)
            if(sql is None or values is None):
                return Response("Can only update optional article fields", status=status.HTTP_400_BAD_REQUEST)
            cursor.execute(sql, values)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete authors, articles
@api_view(('DELETE',))
def DeleteAuthor(req):
    serializer = AuthorSerializer(data=req.data)
    if(serializer.is_valid()):
        with connection.cursor() as cursor:
            name = serializer.data['name']
            affiliation = serializer.data['affiliation']
            name = name.replace('+', ' ').lower()
            affiliation = affiliation.replace('+', ' ').lower()
            cursor.execute("DELETE FROM AUTHORS WHERE LOWER(name) = %s AND LOWER(affiliation) = %s", [name, affiliation])
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('DELETE',))
def DeleteArticle(req):
    serializer = ArticleSerializer(data=req.data)
    if(serializer.is_valid()):
        with connection.cursor() as cursor:
            sql, values = delete_article_sql(serializer.data)
            print(sql)
            print(values)
            cursor.execute(sql, values)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_article_sql(cereal):
    article_fields = ['affiliation', 'pub_title', 'pub_year', 'pub_url', 'citations', 'citedby', 'journal','pub_author']
    sql = 'INSERT INTO Articles(name'
    form = " VALUES (%s"
    values = [cereal['name'].replace("+", ' ')]
    for field in article_fields:
        if(field in cereal):
            values.append(cereal[field].replace('+', ' '))
            sql += ', ' + field
            form += ', ' + '%s'
    sql += ')'
    form += ')'
    result = sql + form
    return result, values

def delete_article_sql(cereal):
    article_fields = ['affiliation', 'pub_title', 'pub_year', 'pub_url', 'citations', 'citedby', 'journal','pub_author']
    sql = 'DELETE FROM Articles WHERE LOWER(name) = %s'
    values = [cereal['name'].replace("+", ' ').lower()]
    for field in article_fields:
        if(field in cereal):
            values.append(cereal[field].replace('+', ' ').lower())
            sql += ' AND LOWER(' + field + ") = %s"
    return sql, values

def update_article_sql(cereal):
    optional_article_fields = ['pub_year', 'pub_url', 'citations', 'citedby', 'journal','pub_author']
    values = []
    sql = 'SET '
    for field in optional_article_fields:
        if(field in cereal):
            values.append(cereal[field].replace('+', ' '))
            sql += field + ' = %s '
    # there are no optional parameters to update
    if(len(values) == 0):
        return None, None
    sql = 'UPDATE Articles ' + sql + "WHERE " + 'name = %s AND affiliation = %s AND pub_title = %s'
    values.append(cereal['name'].replace('+', ' '))
    values.append(cereal['affiliation'].replace('+', ' '))
    values.append(cereal['pub_title'].replace('+', ' '))
    return sql, values

@api_view(('GET',))
def TopicDetailByName(req,topic):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT Articles.id as id,Articles.pub_title as title '
            'FROM Topics LEFT JOIN Articles ON Topics.article_id=Articles.id'
            'WHERE Topics.assumed_topic = %s', [topic])
    print(cursor.fetchall())
