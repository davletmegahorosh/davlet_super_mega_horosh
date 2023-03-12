from rest_framework.response import Response
from rest_framework import status
from elreiprimo.serializers import DirectorSerializer,DirectorCreateSerializer
from elreiprimo.models import Director
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    def create_director(self,request, *args, **kwargs):
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

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'