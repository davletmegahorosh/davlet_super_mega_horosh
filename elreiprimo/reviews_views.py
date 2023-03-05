from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElprimoSerializer, DirectorSerializer, ReviewSerializer,\
ElprimoCreateSerializer, DirectorCreateSerializer, ReviewCreateSerializer
from .models import Elprimo, Director, Review
from django.db.models import Avg

@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        elprimo_id = serializer.validated_data.get('elprimo_id')
        review = Review.objects.create(text=text, stars=stars, elprimo=elprimo_id)
        return Response(data={'message': 'vse ok',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail' : 'review not found!!!'},
                    status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many = False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.elprimo_id = serializer.validated_data.get('elprimo_id')
        review.save()
        return Response(data={'message': 'Data recived!!!',
                              'review': ReviewSerializer(review).data})



@api_view(['GET'])
def average_stars(request):
    average = Review.objects.aggregate(Avg('stars'))
    return Response({'average_rating' : average})

