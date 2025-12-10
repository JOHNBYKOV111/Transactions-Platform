import os
import logging
from pathlib import Path

# Абсолютный путь к корню проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки для статических файлов
STATIC_URL = '/static/'                 # объявляем STATIC_URL
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Каталог для сбора статики

# Настройки Redis
CELERY_BROKER_URL = 'redis://localhost:6379/0'     # Redis сервер для очередей задач
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' # Redis для хранения статусов

# Настройки Celery
CELERY_ACCEPT_CONTENT = ['json']      # Разрешены задачи в формате JSON
CELERY_TASK_SERIALIZER = 'json'       # Сериализация задач в JSON при отправке в брокер
CELERY_RESULT_SERIALIZER = 'json'     # Сериализация результатов задач в JSON
CELERY_TASK_TRACK_STARTED = True      # Отслеживание статуса запуска задачи
CELERY_TASK_IGNORE_RESULT = False     # Результат выполнения не игнорируется (результат сохраняется)
CELERY_TASK_ALWAYS_EAGER = False      # Запуск задачи в фоне, а не в eager-режиме
CELERY_TASK_EAGER_PROPAGATES = True   # Ошибки при eager-запуске возвращаются (для отладки)

# Настройки Django
INSTALLED_APPS = [
	'django.contrib.admin',       # Администрация Django для управления сайтом
	'django.contrib.auth',        # Система аутентификации и авторизации пользователей
	'django.contrib.contenttypes',# Фреймворк для определения типов контента в моделях
	'django.contrib.sessions',    # Поддержка сессий пользователей
	'django.contrib.messages',    # Поддержка сообщений для отображения уведомлений пользователям
	'django.contrib.staticfiles', # Управление статическими файлами (CSS, JS, изображения)
	'payments',                   # приложение
	'rest_framework',             # библиотека для REST API
]

# основной URL
ROOT_URLCONF = 'payout_project.urls'

# SQLite база данных для локальной разработки
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# Настройки REST framework
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': [
		'rest_framework.renderers.JSONRenderer',  # Ответы API только в JSON формате
	],
	'DEFAULT_PARSER_CLASSES': [
		'rest_framework.parsers.JSONParser',      # Принимаем запросы только в JSON
	],
}


# Обработчики запросов/ответов
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',             # Защита от HSTS, security headers-атак
	'django.contrib.sessions.middleware.SessionMiddleware',      # Сессии пользователей
	'django.middleware.common.CommonMiddleware',                 # Общие функции
	'django.middleware.csrf.CsrfViewMiddleware',                 # Защита от CSRF-атак
	'django.contrib.auth.middleware.AuthenticationMiddleware',   # Аутентификация
	'django.contrib.messages.middleware.MessageMiddleware',      # Отображение сообщений
	'django.middleware.clickjacking.XFrameOptionsMiddleware',    # Защита от clickjacking-атак
]


# Настройки шаблонов
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates', # Настройка шаблонов Django
		'DIRS': [],                                                  # Пути к кастомным шаблонам
		'APP_DIRS': True,                                            # Автоматический поиск шаблонов
		'OPTIONS': {
			'context_processors': [                                    # Добавление переменныых в шаблоны
				'django.template.context_processors.debug',              # Информация для отладки
				'django.template.context_processors.request',            # Добавление в шаблон объекта request
				'django.contrib.auth.context_processors.auth',           # Данные аутентификации пользователя
				'django.contrib.messages.context_processors.messages',   # Уведомления
			],
		},
	},
]


# Сгенерированный секретный ключ
SECRET_KEY = '5e99f1801627560a04d2fbf1c7148df96aa4148b121954aa548be039bb165adb'


# Настройки логирования
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
			'celery_file': {
					'level': 'INFO',
					'class': 'logging.FileHandler',
					'filename': os.path.join(BASE_DIR, 'logs', 'celery', 'celery.log'),
					'formatter': 'verbose',
			},
			'celery_beat_file': {
					'level': 'INFO',
					'class': 'logging.FileHandler',
					'filename': os.path.join(BASE_DIR, 'logs', 'celery', 'celery_beat.log'),
					'formatter': 'verbose',
			},
	},
	'loggers': {
			'celery': {
					'handlers': ['celery_file'],
					'level': 'INFO',
					'propagate': False,
			},
			'celery.beat': {
					'handlers': ['celery_beat_file'],
					'level': 'INFO',
					'propagate': False,
			},
	},
	'formatters': {
			'verbose': {
					'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
					'style': '%',
			},
	},
}

# Режим отладки
DEBUG = True
