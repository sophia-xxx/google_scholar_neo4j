from rest_framework import serializers
from .models import Author


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            #'id',
            'name',
            'affiliation',
            #'attributes',
        )
        model = Author
