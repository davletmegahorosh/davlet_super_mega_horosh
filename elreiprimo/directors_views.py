from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElprimoSerializer, DirectorSerializer, ReviewSerializer,\
ElprimoCreateSerializer, DirectorCreateSerializer, ReviewCreateSerializer
from .models import Elprimo, Director, Review

@api_view(['GET','POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')
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
        serializer = DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'message' : 'Data recived!!!',
                                'director' : DirectorSerializer(director).data})

