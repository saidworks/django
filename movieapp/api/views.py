from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer,RatingSerializer
from .models import Movie,Rating

# Create your views here. example of view as function
def test(request):
    return render(request,template_name='test.html')

#Class viewsets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer