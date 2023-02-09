from rest_framework import serializers
from .models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = NewUser
        fields = (
            'email', 
            'user_name', 
            'first_name', 
            'last_name', 
            'mob_num',
            'password', 
            'confirm_password'
        )

    # validation if password and confirm_password matches
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match")
        return data

    # perform create using NewUser.objects.create_user()
    def create(self, validated_data):
        user = NewUser.objects.create_user(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mob_num=validated_data['mob_num'],
            password=validated_data['password']
        )
        return user