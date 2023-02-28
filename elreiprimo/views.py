from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElprimoSerializer, DirectorSerializer, ReviewSerializer
from .models import Elprimo, Director, Review
from django.db.models import Avg

@api_view(['GET', 'POST'])
def elprimo_list_api_view(request):
    if request.method == 'GET':
        elprimos = Elprimo.objects.all()
        serializer = ElprimoSerializer(elprimos, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        des = request.data.get('des')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        elprimo = Elprimo.objects.create(name=name, des=des, duration=duration, director_id=director_id)
        return Response(data={'message': 'vse ok',
                              'elprimo' : ElprimoSerializer(elprimo).data},
                                status=status.HTTP_201_CREATED)

        # product.tags.set(tags)
        # product.save()
        # return Response(data={'message' : 'data recived!!!',
        #                       'elprimo' : ElprimoSerializer(elprimo).data},
        #                 status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def elprimo_detail_api_view(request, id):
        try:
            elprimo = Elprimo.objects.get(id=id)
        except Elprimo.DoesNotExist:
            return Response(data={'detail' : 'el primo not found!!!'},
                            status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ElprimoSerializer(elprimo, many = False)
            return Response(data=serializer.data)
        elif request.method == 'DELETE':
            elprimo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            elprimo.name = request.data.get('name')
            elprimo.des = request.data.get('des')
            elprimo.duration = request.data.get('duration')
            elprimo.director_id = request.data.get('director_id')
            # elprimo.tags.set(request.data.get('tags'))
            elprimo.save()
            return Response(data={'message' : 'Data recived!!!',
                                  'elprimo' : ElprimoSerializer(elprimo).data})
@api_view(['GET','POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'vse ok',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail' : 'director not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many = False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message' : 'Data recived!!!',
                                'director' : DirectorSerializer(review).data})

@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        elprimo_id = request.data.get('elprimo_id')
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
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.elprimo_id = request.data.get('elprimo_id')
        review.save()
        return Response(data={'message': 'Data recived!!!',
                              'review': ReviewSerializer(review).data})



@api_view(['GET'])
def average_stars(request):
    average = Review.objects.aggregate(Avg('stars'))
    return Response({'average_rating' : average})


@api_view(['GET'])
def test_api(request):
    dict_ = {
        'text' : 'el primo',
        'int' : 100,
        'float' : 9.99,
        'bool' : True,
        'list' : [1,2,3],
    }
    return Response(data = dict_, status=status.HTTP_204_NO_CONTENT)