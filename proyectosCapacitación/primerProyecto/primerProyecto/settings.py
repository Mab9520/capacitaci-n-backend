"""
Django settings for primerProyecto project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path #Permite manejar las rutas

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#Clave para hacer encriptacion NO SE MODIFICA!!!!!
SECRET_KEY = 'e_+ue0m42if@y%g@q1l9l$&pp46^k&g!n_aeb3_6r_fcxds$zr'

# SECURITY WARNING: don't run with debug turned on in production!
#Especifica el error a fondo , en un ambiente produccion se coloca en false
DEBUG = True

#INdica sobre que dns se va a trabajar el proyecto
ALLOWED_HOSTS = ['*']#¡el * acepta todos los host en modo prueba solamente!


# Application definition
#Direccion a todas las apps que se crean
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.users.apps.UsersConfig',
    'rest_framework.authtoken', #aplicacion ya incluida en restFramework
    'apps.workers.apps.WorkersConfig',
]

#scripts necesarios para que django funcione correctamente, se colocan configuraciones de seguridad
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 8,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', #va a crear una bandera (is_active)
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # se envia el token de autenticacion? si no no pasa/
        #globalmente bloquea las vistas
        'apps.users.authorization.TokenAuthenticationUser',
    ),
}
#ruta/archivo principal de las urls
ROOT_URLCONF = 'primerProyecto.urls'

#
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],#rutas donde irán los templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#
WSGI_APPLICATION = 'primerProyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#Configuración para la conexion de la base de datos
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
#Configuramos la base de datos de esta manera
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbCapacitacion',
        'USER' : 'mabe',
        'PASSWORD' : 'password',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}

AUTH_USER_MODEL = 'users.User'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
#Informacion sobre validaciones de passwords para los usuarios del proyecto (NO SE MODIFICA)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True #Internationalization

USE_L10N = True

USE_TZ = False #se coloca en false para respetar la zona horaria que se le especifica en TIME_ZONE


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#provee los archivos estaticos (css, js)
STATIC_URL = '/static/'
