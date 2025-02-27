"""
Django settings for DjangoEcommerce project.

Generated by 'django-admin startproject' using Django 4.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+x^abv3&dg(k_nlc21hne17j8b)oj9s0f@m&&quqkk&md4tto7'






# Application definition

INSTALLED_APPS = [
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'pages',
        'Products',
        'tailwind',
        'theme',
        'django_browser_reload',
        'accounts.apps.AccountsConfig',
        'carts'

]

TAILWIND_APP_NAME = 'theme'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'allauth.account.middleware.AccountMiddleware'

]

ROOT_URLCONF = 'DjangoEcommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR, '../templates'),
        os.path.join(BASE_DIR, '../templates', 'account'),
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Products.context_processors.categories'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoEcommerce.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL= 'media/'

STATICFILES_DIRS = [
    BASE_DIR / '../static'
]

STATIC_ROOT = BASE_DIR/ '../staticfiles'
MEDIA_ROOT = BASE_DIR/ '../static/media'

STATICFILES_STORAGE: "whitenoise.storage.CompressedManifestStaticFilesStorage"

# allauth settings 
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]

ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'
LOGIN_ACCOUNT_URL = 'home'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True
SOCIALACCOUNT_QUERY_EMAIL= ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_AUTO_SIGNUP= True
SOCIALACCOUNT_EMAIL_REQUIRED =ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_STORE_TOKENS =True
SOCIALACCOUNT_ENABLED= True
SOCAIALACCOUNT_ONLY = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_PASSKEY_LOGIN_ENABLED=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'DJANGO_ECCOMERCE'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# sending email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER =config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
