from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElprimoSerializer, DirectorSerializer, ReviewSerializer
from .models import Elprimo, Director, Review

@api_view(['GET'])
def elprimo_list_api_view(request):
    elprimos = Elprimo.objects.all()
    serializer = ElprimoSerializer(elprimos, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def elprimo_detail_api_view(request, id):
    try:
        elprimo = Elprimo.objects.get(id=id)
    except Elprimo.DoesNotExist:
        return Response(data={'detail' : 'el primo not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ElprimoSerializer(elprimo, many = False)
    return Response(data=serializer.data)

@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail' : 'director not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director, many = False)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail' : 'review not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many = False)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def test_api(request):
    dict_ = {
        'text' : 'el primo',
        'int' : 100,
        'float' : 9.99,
        'bool' : True,
        'list' : [1,2,3],
    }
    return Response(data = dict_, status=status.HTTP_204_NO_CONTENT)