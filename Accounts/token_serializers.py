# Accounts/token_serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD  # tells JWT to use email instead of username

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user_id"] = str(user.id)
        token["role"] = user.role          # plain CharField — no cast needed
        token["email"] = user.email
        token["is_staff"] = user.is_staff
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name

        return token