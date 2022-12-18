from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

#Retorna el modelo que utiliza la autenticación de Django para los usuarios
User = get_user_model()

def create_jwt_pair_for_user(user: User):
    """Genera tokens de access y refresh en base a los usuarios que creamos"""
    refresh = RefreshToken.for_user(user)

    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}

    return tokens