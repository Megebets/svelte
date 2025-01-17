from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'last_name', 'first_name', 'middle_name', 'password']

class UserProfileRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'last_name', 'first_name', 'middle_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserProfile(
            phone=validated_data['phone'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
