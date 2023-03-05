from rest_framework import serializers
from .models import Elprimo, Director, Review
from rest_framework.exceptions import ValidationError
class DirectorSerializer(serializers.ModelSerializer):
    movie_number = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movie_number'.split()
    def get_movie_number(self, director):
        return director.elprimo_set.count()
class ElprimoDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ElprimoSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # tag = TagSerializer(many=True)
    # tag_name_list = serializers.SerializerMethodField()
    director = ElprimoDirectorSerializer()
    elprimo_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Elprimo
        fields = 'id name des duration elprimo_reviews director'.split()   #( tag category category_name tag_name_list)


class ElprimoCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    des = serializers.CharField()
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()
    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('this director does not exist')
        return director_id

class DirectorCreateSerializer(serializers.Serializer):
    name = serializers.CharField()

class ReviewCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(max_value=5, min_value=1)
    elprimo_id = serializers.IntegerField()
    def validate_elprimo_id(self, elprimo_id):
        try:
            Director.objects.get(id=elprimo_id)
        except Elprimo.DoesNotExist:
            raise ValidationError('this elprimo does not exist')
        return elprimo_id

    # def get_tag_name_list(self,elprimo):
    #     lisst = []
    #     for tag in elprimo.tags.all():
    #         lisst.append(tag.name)
    #     return lisst

    # class CategorySerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Category
    #         fields = 'id name'.split()
    #
    # class TagSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Tag
    #         fields = 'id name'.split()
