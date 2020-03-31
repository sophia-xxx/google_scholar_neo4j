from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            #'id',
            'name',
            'affiliation',
        )
        model = Author
