from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView 


class token_serializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user)
        token['username'] = str(user)
        return token

class token_view(TokenObtainPairView):

    serializer_class = token_serializer