from pathlib import Path
import environ


env = environ.Env(DEBUG=(bool, True))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(".env")

# SECURITY_WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY_WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    # authentication
    "rest_framework.authtoken",
    # documentation
    "drf_yasg",
    # local apps
    "apps.core",
    "apps.common",
    "apps.metadata",
    "apps.novels",
    "apps.chapters",
    "apps.users",
    "apps.teams",
    "apps.authentication",
    "apps.oauth",
    "apps.libraries",
    "apps.bookmarks",
    "apps.notifications",
    "apps.comments",
    "apps.converter",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # 'allauth.account.middleware.AccountMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middlewares.RequestLoggingMiddleware",
]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {"default": env.db()}

AUTH_USER_MODEL = "users.User"

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
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "EXCEPTION_HANDLER": "apps.core.exceptions.api_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "apps.core.pagination.LimitOffsetPagination",
}

# this setting also works for email reset
PASSWORD_RESET_TIMEOUT = 5 * 60

# Email setup
EMAIL_CONFIRM_REDIRECT_BASE_URL = BASE_URL + "/email/confirm/"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# oauth
# google
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET")
GOOGLE_CLIENT_PROJECT_ID = env("GOOGLE_CLIENT_PROJECT_ID")


# media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[{levelname}:{asctime}]: {message}", "style": "{"},
    },
    "handlers": {
        "debug_file": {
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 100,
            "backupCount": 5,
            "filename": "./logs/debug.log",
        },
        "request_file": {
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 100,
            "backupCount": 5,
            "filename": "./logs/requests.log",
        },
        "console": {
            "level": "INFO",
            "formatter": "simple",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "drf_requests": {
            "level": "DEBUG",
            "handlers": ["request_file"],
        },
        "apps": {"level": "INFO", "handlers": ["console"]},
        "": {
            "level": "DEBUG",
            "handlers": ["debug_file"],
        },
    },
}

DEFAULT_LIBRARY_NAMES = ["Читаю", "Буду читать", "Прочитано", "Любимые"]

CONVERTER_CSS_FILE = BASE_DIR / "static/file.css"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
