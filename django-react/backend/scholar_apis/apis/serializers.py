from rest_framework import serializers
from .models import Author, Article


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    affiliation = serializers.CharField()
    # class Meta:
    #     fields = (
    #         #'id',
    #         'name',
    #         'affiliation',
    #     )
    #     model = Author
class ArticleSerializer(serializers.Serializer):
    name = serializers.CharField()
    affiliation = serializers.CharField()
    pub_title = serializers.CharField()
    pub_year = serializers.CharField(required=False)
    pub_url = serializers.CharField(required=False)
    citations = serializers.CharField(required=False)
    citedby = serializers.CharField(required=False)
    journal = serializers.CharField(required=False)
    pub_author = serializers.CharField(required=False)
    # class Meta:
    #     fields = (
    #         #'id',
    #         'name',
    #         'affiliation',
    #         'pub_title',
    #         'pub_year',
    #         'pub_url',
    #         'citations',
    #         'citedby',
    #         'journal',
    #         'pub_author',
    #     )
    #     model = Article
