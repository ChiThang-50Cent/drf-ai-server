from django.db import models
from django.contrib.auth import models as auth_models

from uuid import uuid4

# Create your models here.
class User(auth_models.AbstractBaseUser):
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(verbose_name="Email",max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        api_key = API_Key(user=self)
        api_key.save()
        

class API_Key(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    key = models.UUIDField(
        primary_key=True,
        default= uuid4,
        editable=False
    )

    def __str__(self) -> str:
        return f'{self.user}_{self.key}'