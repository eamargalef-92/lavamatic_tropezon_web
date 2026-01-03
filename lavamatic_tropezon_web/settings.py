"""
Django settings for lavamatic_tropezon_web project.
"""

import os
from pathlib import Path

# =========================
# BASE
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY / ENV
# =========================
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-only-change-in-production"
)

DEBUG = os.environ.get("DEBUG", "True").strip().lower() in ("true", "1", "yes")


# =========================
# HOSTS (RENDER / LOCAL)
# =========================
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    # Render setea RENDER_EXTERNAL_HOSTNAME = "tu-app.onrender.com"
    ALLOWED_HOSTS = [
        RENDER_EXTERNAL_HOSTNAME,
        ".onrender.com",
    ]

    CSRF_TRUSTED_ORIGINS = [
        f"https://{RENDER_EXTERNAL_HOSTNAME}",
    ]

    # Render termina TLS en su proxy; Django debe saber que la request original fue HTTPS
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
else:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "webinfo",
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise (static files en Render)
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# URLS / TEMPLATES
# =========================
ROOT_URLCONF = "lavamatic_tropezon_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "lavamatic_tropezon_web.wsgi.application"


# =========================
# DATABASE
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise storage (cache + hash)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# =========================
# DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
