from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Place, Portfolio, Category
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class PortfolioSerializer(serializers.ModelSerializer):
    cat = CategorySerializer(read_only=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Portfolio
        fields = '__all__'
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None