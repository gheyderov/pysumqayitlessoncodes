import time
from celery import shared_task
from django.template.loader import render_to_string
from core.models import Subscriber
from stories.models import Recipe
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def export_data():
    print('Export Start!')
    time.sleep(10)
    print('Export End!')


@shared_task
def send_email_to_subscribers():
    email_list = Subscriber.objects.values_list('email', flat=True)
    recipes = Recipe.objects.all()[:3]
    subject = 'Latest Posts'
    message = render_to_string('email-subscribers.html', {
        'recipes': recipes
    })
    mail = EmailMultiAlternatives(
        subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'HTML'
    mail.send()
