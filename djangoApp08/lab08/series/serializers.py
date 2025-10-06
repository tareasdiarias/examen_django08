from rest_framework import serializers
from .models import Serie
from .models import Category


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')