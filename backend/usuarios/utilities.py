from rest_framework_simplejwt.tokens import RefreshToken

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    print(refresh.access_token)
    return str(refresh.access_token)