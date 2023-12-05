from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2",]


    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["username"]
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"Message": "Both passwords must match"})
        
        user.set_password(password)
        user.save()
        return user