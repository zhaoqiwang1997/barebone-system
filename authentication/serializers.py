from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'birthday']
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        
        instance.save()
        return instance