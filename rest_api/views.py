# implement your views here
from datetime import datetime

import django_filters.rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_api.models import Weather
from rest_api import model_filters
from rest_api.serializers import WeatherSerializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter


class WeatherListView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filterset_class = model_filters.WeatherFilter
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    #ordering_fields = ['date', ]

    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherView(APIView):
    def get(self, request, id):
        weather_obj = Weather.objects.filter(id=id)
        if weather_obj:
            serializer = WeatherSerializer(weather_obj[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'no weather found with id'}, status=status.HTTP_404_NOT_FOUND)


