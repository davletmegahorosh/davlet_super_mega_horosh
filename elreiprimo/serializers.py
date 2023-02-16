from rest_framework import serializers
from .models import Elprimo, Director, Review

class ElprimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elprimo
        fields = ['id', 'name', 'des', 'duration','director']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'movie']
