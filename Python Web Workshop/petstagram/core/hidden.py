class ThisProject:
    SECRET_KEY = 'django-insecure-ma)$f5cgl1&uj4jrv%*e^ky7^^%k^ikfi4#uh^x4kpz6jx7fd+'
    USER = 'root'
    PASSWORD = 'root'
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "petstagram-db",
            "USER": 'root',
            "PASSWORD": 'root',
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
