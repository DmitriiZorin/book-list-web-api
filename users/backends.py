import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'ApiKey'

    def authenticate(self, request):
        request.user = None

        headers = request.headers
        token = headers.get(self.authentication_header_prefix, None)
        if (token is None):
            return None
        
        print(token)
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        except Exception:
            msg = 'Ошибка аутентификации. Невозможно декодировать токен.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'Пользователь соответствующий данному токену не найден.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)