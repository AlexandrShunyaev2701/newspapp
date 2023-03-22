from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task
from .models import *
from datetime import *

@shared_task
def send_message(preview, pk, headline, subscribers):
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
    post = Post.objects.get(pk)
    categories = post.categories.all()
    subscribers_email = []
    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_email += [s.email for s in subscribers]

    send_message(post.preview(), post.pk, post.headline, subscribers_email)