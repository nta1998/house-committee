# ------import------
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Profile, Ads, Pool, Payment_ads, Vote, Chat, Online, Product, Building
# ------login serializers return token-------


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token
# -----model serializers-----


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Profile.objects.create(**validated_data, user=user)


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Ads.objects.create(**validated_data, user=user)


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Pool.objects.create(**validated_data, user=user)


class PayAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_ads
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Payment_ads.objects.create(**validated_data, user=user)


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

    def create(self, validated_data):
        return Vote.objects.create(**validated_data)


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)


class OnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

    def create(self, validated_data):

        return Building.objects.create(**validated_data)
