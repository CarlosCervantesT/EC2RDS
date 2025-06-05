import os
from pathlib import Path

# ------------------------------
#  RUTAS BÁSICAS Y SECRET_KEY
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Nunca dejes la clave en texto plano en producción.
# En su lugar, ponla en una variable de entorno llamada DJANGO_SECRET_KEY
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-temporal-para-dev")

# ------------------------------
#  DEBUG y ALLOWED_HOSTS
# ------------------------------
# DEBUG debe estar en False en producción. Si la variable no existe, se asume False.
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() in ("true", "1", "yes")

# Puedes configurar directamente la IP del servidor si no usas variables de entorno
ALLOWED_HOSTS = ["3.19.56.170"]

# ------------------------------
#  APPS INSTALADAS / MIDDLEWARE
# ------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "appi",  # tu app personalizada
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "interfaz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Puedes añadir si tienes templates globales
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "interfaz.wsgi.application"

# ------------------------------
#  BASE DE DATOS (RDS) POR ENV VARS
# ------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DJANGO_DB_NAME", "db_default_name"),
        "USER": os.environ.get("DJANGO_DB_USER", "user_default"),
        "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD", "password_default"),
        "HOST": os.environ.get("DJANGO_DB_HOST", "localhost"),
        "PORT": os.environ.get("DJANGO_DB_PORT", "5432"),
    }
}

# ------------------------------
#  VALIDADORES DE CONTRASEÑA
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ------------------------------
#  LOCALIZACIÓN
# ------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------------------
#  ARCHIVOS ESTÁTICOS
# ------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# ------------------------------
#  CAMPO DE PK POR DEFECTO
# ------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
