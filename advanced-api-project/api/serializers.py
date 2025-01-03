from rest_framework import serializers
from .models import Book, Author
from datetime import datetime



class AuthorSerializer(serializers.ModelSerializer):
    """This is a serializer class that serializes and deserializes the author object into json it contains a single field for output """
    class Meta:
        model = Author
        fields = ['name']
        
    


class BookSerializer(serializers.ModelSerializer):
    """This is a serializer class that serializes and deserializes the book object into json it contains a single field for output
        it also has a nested AuthorSerializer class which determines the flow of how the data is been passed or represented on every http request
    """
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = "__all__"
    
    def validate(self, data):
        """"This checks the data that is passed during the post, put or patch method and validates the cond. set"""
        current_date = datetime.now()
        if data['publication_year'] > current_date.year:
            raise serializers.ValidationError("Publication date is way ahead of the current year")

        return data
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        name = author_data['name']
        try:
            author = Author.objects.get(name=name)
            book = Book.objects.create(**validated_data, author=author)
        except Author.DoesNotExist:
            author = Author.objects.create(name=name)
            book = Book.objects.create(**validated_data, author=author)
        book.save()
        return book
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author = instance.author
    
        instance.title = validated_data.get('title', instance.title)
        instance.publication_year = validated_data.get('publication_year', instance.publication_year)

        # save the author
        author.save()
        # save the book object and return it
        instance.save()
        return instance
        
