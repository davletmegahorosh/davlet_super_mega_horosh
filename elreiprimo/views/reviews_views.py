from rest_framework.response import Response
from rest_framework import status
from elreiprimo.serializers import ReviewSerializer, ReviewCreateSerializer
from elreiprimo.models import Review
from django.db.models import Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

class RewiewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def create_review(self,request, *args, **kwargs):
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

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

class AverageStarsAPIView(APIView):
    @staticmethod
    def average_stars(request):
        average = Review.objects.aggregate(Avg('stars'))
        return Response({'average_rating' : average})