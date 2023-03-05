from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElprimoSerializer, DirectorSerializer, ReviewSerializer,\
ElprimoCreateSerializer, DirectorCreateSerializer, ReviewCreateSerializer
from .models import Elprimo, Director, Review
from django.db.models import Avg

@api_view(['GET', 'POST'])
def elprimo_list_api_view(request):
    if request.method == 'GET':
        elprimos = Elprimo.objects.all()
        serializer = ElprimoSerializer(elprimos, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ElprimoCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data = serializer.errors,
                            status = status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')
        des = serializer.validated_data.get('des')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
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
            serializer = ElprimoCreateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            elprimo.name = serializer.validated_data.get('name')
            elprimo.des = serializer.validated_data.get('des')
            elprimo.duration = serializer.validated_data.get('duration')
            elprimo.director_id = serializer.validated_data.get('director_id')
            # elprimo.tags.set(request.data.get('tags'))
            elprimo.save()
            return Response(data={'message' : 'Data recived!!!',
                                  'elprimo' : ElprimoSerializer(elprimo).data})

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