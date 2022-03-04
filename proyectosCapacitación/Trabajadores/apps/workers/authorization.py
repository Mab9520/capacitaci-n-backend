#Aquí colocaremos lo que mando Gera y volvemos a vistas
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from apps.workers.models import Worker


class TokenAuthenticationUser(TokenAuthentication):

    def authenticate_credentials(self, key): #la key que recibe el metodo YA DEFINIDO DE LA CLASE TokenAuthentication
        #try/except: Intenta realizar esta operacion, si no lo encuentro entro a la excepcion para no romper el flujo
        try:
            token = Token.objects.get(key=key) #obtemos el token

        except Exception as e:
            raise AuthenticationFailed({"status": ["El token fue eliminado o no es valido."]})

        if not token.user.is_active:
            raise AuthenticationFailed({"status": ["Usuario no esta activo"]})

        return token.user, token