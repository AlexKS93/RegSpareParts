from django.contrib.auth.models import AbstractUser
#from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
#from users.validators import validate_username

ADMIN = 'admin'
USER = 'auth_user'
ANON = 'guest'


class User(AbstractUser):
    ROLES = [
        (ADMIN, 'admin'),
        (USER, 'user'),
    ]

    username = (models
                .CharField("Логин",
                           max_length=150,
                           unique=True,
                           null=False,
                        #    validators=[#validate_username,
                        #                RegexValidator(regex='^[\w.@+-]+\Z',
                        #                               message='Использованы не разрешенные символы'),
                        #               ]
                                ))
    email = models.EmailField("Email",
                              max_length=254,
                              unique=True,
                              null=False)
    first_name = models.CharField("Имя",
                                  max_length=150,
                                  null=True)
    last_name = models.CharField("Фамилия",
                                 max_length=150,
                                 null=True)
    role = models.CharField('Доступ',
                            choices=ROLES,
                            max_length=9,
                            default=USER,
                            null=True)
    password = models.CharField("Пароль",
                                max_length=150,)
    
    position = models.CharField("Должность",
                                max_length=150,)


