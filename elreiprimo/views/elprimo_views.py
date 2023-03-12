from rest_framework.response import Response
from rest_framework import status
from elreiprimo.serializers import ElprimoSerializer,ElprimoCreateSerializer
from elreiprimo.models import Elprimo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class ElprimoListAPIView(ListCreateAPIView):
    queryset = Elprimo.objects.all()
    serializer_class = ElprimoSerializer
    pagination_class = PageNumberPagination
    def elprimo_create(self,request, *args, **kwargs):
        if request.method == 'GET':
            elprimo = Elprimo.objects.all()
            serializer = ElprimoSerializer(elprimo, many=True)
            return Response(data=serializer.data)
        elif request.method == 'POST':
            serializer = ElprimoCreateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            name = serializer.validated_data.get('name')
            des = serializer.validated_data.get('des')
            duration = serializer.validated_data.get('duration')
            director_id = serializer.validated_data.get('director_id')
            elprimo = Elprimo.objects.create(name=name, des=des, duration=duration, director_id=director_id)
            return Response(data={'message': 'vse ok',
                                  'elprimo': ElprimoSerializer(elprimo).data},
                            status=status.HTTP_201_CREATED)

class ElprimoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Elprimo.objects.all()
    serializer_class = ElprimoSerializer
    lookup_field = 'pk'

class TestAPIView(APIView):
    @staticmethod
    def test_api(request):
        dict_ = {
            'text' : 'el primo',
            'int' : 100,
            'float' : 9.99,
            'bool' : True,
            'list' : [1,2,3],
        }
        return Response(data = dict_, status=status.HTTP_204_NO_CONTENT)