from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task
from .models import *


@shared_task
def send_message(pk):
    preview = Post.text[:124]
    headline = Post.headline
    subscribers = Category.subscribers

    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=headline,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()
    
    
@shared_task
def notify_about_new_post(pk):
    headline = Post.headline
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_email = []
    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_email += [s.email for s in subscribers]

    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': headline,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=headline,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()