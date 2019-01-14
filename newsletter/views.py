from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives  # noqa
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST
from premailer import transform  # noqa
from .models import Newsletter, Subscriber


@login_required
def newsletter_list(request):
    params = {
        'section': 'Newsletters',
        'newsletters': Newsletter.objects.all()
    }
    return render(request, 'newsletter/newsletter_list.html', params)


@login_required
def newsletter_view(request, date=None):
    newsletter = get_object_or_404(Newsletter, published=date)
    params = {
        'section': 'Newsletters',
        'newsletter': newsletter,
    }
    return render(request, 'newsletter/newsletter_view.html', params)


@login_required
def newsletter_mockup(request, date=None):
    newsletter = get_object_or_404(Newsletter, published=date)
    params = {
        'section': 'Newsletters',
        'newsletter': newsletter,
    }
    return render(request, 'newsletter/email/newsletter.html', params)


@require_POST
@login_required
def newsletter_send(request, date=None):
    newsletter = get_object_or_404(Newsletter, published=date)  # noqa
    params = {
        'section': 'Newsletters',
        'newsletter': newsletter,
    }

    subject = 'CI Newsletter'
    sender = 'antonio@lopez.io'
    html_message = transform(render_to_string(
        'newsletter/email/newsletter.html', params))
    plain_message = strip_tags(html_message)
    bcc_recipients = [s.email for s in Subscriber.objects.all()]
    msg = EmailMultiAlternatives(
        subject, plain_message, sender, [], bcc_recipients)
    msg.attach_alternative(html_message, "text/html")
    msg.send()

    return render(request, 'newsletter/newsletter_sent.html', params)
