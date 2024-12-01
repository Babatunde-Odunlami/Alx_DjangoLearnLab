from rest_framework import serializers
from .models import Author, Book

#Book serializer that with all fields serialized from the Book modle instance
class BookSerializer(serializers.ModelSerializer):
    '''creating a serializer for the Book model'''
    model = Book
    fields = '__all__'

    # A validator to ensure that the publication year can be the present year or past
    def validate(self,data):
        '''future proof validator'''
        if data['publication_year'] > 2024:
            raise serializers.ValidationError("Publication year can not be in the future.")
        return data

#Author serializer that has the field 'name' and nested Bookserializer 
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    Meta:
        model = Author
        fields = ['name']
