from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from rest_framework.decorators import authentication_classes, permission_classes


class CustomUserSerializer(serializers.ModelSerializer):
    queryset = CustomUser.objects.all()

    def create(self, validated_data):
        """
        Create and return a new `CustomUser` instance, given the validated data.
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `CustomUser` instance, given the validated data.
        """
        for attr, value in validated_data.items():
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
                
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {"write_only": True}}
        fields = ['name', 'email', 'password', 'phone', 'is_active', 'is_staff', 'is_superuser']
