from django.db import models
from core.validators import validate_gmail

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    name = models.CharField('Adiniz', max_length=100, unique=True)
    email = models.EmailField('Email', max_length=100)
    subject = models.CharField('Mövzu', max_length=155)
    message = models.TextField('Mesaj')

    def __str__(self):
        return self.name
    

class Subscriber(AbstractModel):
    email = models.EmailField('email', max_length=155, unique=True)

    def __str__(self) -> str:
        return self.email