from rest_framework import serializers
from .models import NewUser

# class RegisterUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=5, write_only=True)
#     # confirm_password = serializers.CharField(write_only=True)
    
#     class Meta:
#         model = NewUser
#         fields = (
#             'email',
#             'user_name',
#             'first_name',
#             'last_name',
#             'mob_num',
#             'password',
#         )
#         extra_kwargs = {'password': {'write_only': True}}

#         # def validate(self, data):
#         #     password = data.get('password')
#         #     if password != data['confirm_password']:
#         #         raise serializers.ValidationError("Passwords do not match")
#         #     return data

#         def create(self, validated_data):
#             password = validated_data.pop('password', None)
#             instance = self.Meta.model.object(**validated_data)
#             if password is not None:
#                 hashed_pass = make_password(password)
#                 instance.set_password(hashed_pass)
#             instance.save()
#             return instance

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

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match")
        return data

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

class ForgetPassSerializer(serializers.Serializer):
    pass