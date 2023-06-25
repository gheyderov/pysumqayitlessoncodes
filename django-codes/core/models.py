from django.db import models

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    name = models.CharField('Adiniz', max_length=100)
    email = models.EmailField('Email', max_length=100)
    subject = models.CharField('Mövzu', max_length=155)
    message = models.TextField('Mesaj')