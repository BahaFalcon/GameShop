from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import filters

from .models import Game, Genre
from .serializers import GameSerializer, GenreSerializer

class GameViewSet(viewsets.ModelViewSet):

    serializer_class = GameSerializer
    # pagination_class = ProductViewSetPagination

    def get_queryset(self):
        return Game.objects.filter(available=True)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        genre = Genre.objects.get(pk=pk)
        return Response({'genre': genre.title})
