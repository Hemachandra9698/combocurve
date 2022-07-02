from rest_api.models import Weather
import django_filters


class WeatherFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(method='char_filter')

    def char_filter(self, qs, name, value):
        value_lst = value.split(',')
        value_lst = [value.casefold() for value in value_lst]
        return qs.filter(city__in=value_lst).order_by('id')

    class Meta:
        model = Weather
        exclude = 'temperatures'
