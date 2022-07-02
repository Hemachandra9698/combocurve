from datetime import datetime
from rest_framework import serializers
from rest_api.models import Weather
# Implement your serializers here


class WeatherSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    city = serializers.CharField()

    def validate_date(self, date_value):
        if date_value:
            return datetime.strptime(str(date_value), '%Y-%m-%d').date()
        return serializers.ValidationError("Required date while storing weather data")

    def validate_city(self, value):
        if value:
            return value.casefold()
        return serializers.ValidationError("Required city while storing weather data")

    class Meta:
        model = Weather
        fields = '__all__'
