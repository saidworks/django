
from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)
urlpatterns = [
    path('', include(router.urls)),
    #path('new/', views.test),

]
