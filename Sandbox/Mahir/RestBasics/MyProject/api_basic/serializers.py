from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validate_data):
        return Article.objects.create(validate_data)

    def update(self, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('title', instance.author)
        instance.email = validate_data.get('title', instance.email)
        instance.date = validate_data.get('title', instance.date)
        instance.save()
        return instance