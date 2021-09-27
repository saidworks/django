from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MovieSerializer,RatingSerializer
from .models import Movie,Rating

# Create your views here. example of view as function
def test(request):
    return render(request,template_name='test.html')

#Class viewsets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail = True,methods = ['POST','GET'])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:
            print(pk)
            response = {'message':'it is working'}
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer