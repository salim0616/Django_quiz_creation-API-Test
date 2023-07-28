from rest_framework import serializers
from users.models import User
import hashlib

class UserRegisterSerializer(serializers.ModelSerializer):
    uid=serializers.UUIDField()

    class Meta:
        model=User
        fields='__all__'

    def create(self,validated_data):
        validated_data['password']=hashlib.md5(validated_data.get("password").encode()).hexdigest()
        return User.objects.create(**validated_data)