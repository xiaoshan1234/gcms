"""
Django settings for gcms project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 自定义常数
COMPANY_NAME = "上党小山"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t3%&fx8#5&*lqo4d&fl+(ovy)+9pi@m99e=d0#x_gs2@u$f$=&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_index',
    'app_staff_ms',
    'app_bdms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gcms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'gcms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# 模板中的 'static' tag 会在 url 添加此前缀
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "collected_static/"
# 指定静态文件寻找路径
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# 指定静态文件寻找引擎
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder', # 文件引擎，与 STATICFILES_DIRS 搭配使用
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', # app 引擎，会在注册的 app 的目录下寻找
]

# 模板中的 'media' tag 会在 url 添加此前缀
MEDIA_URL = '/media/' # 对外的 url 访问路径
MEDIA_ROOT = BASE_DIR / 'media' # 上传文件存储路径

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import logging

# 日志工厂生产日志工具
MainLogger = logging.getLogger("MyLogger") 
# 日志工厂生产日志容器
fileHandler = logging.FileHandler(BASE_DIR / "gcms.log", mode="a+")
# 日志工厂生产日志格式
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 设置日志格式
fileHandler.setFormatter(file_format)
# 设置日志容器
MainLogger.addHandler(fileHandler)
# 设置日志过滤器
MainLogger.setLevel(logging.INFO)
