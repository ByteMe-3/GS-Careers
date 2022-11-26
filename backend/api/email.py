from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_email():
    message = EmailMultiAlternatives(
        subject="subject",
        body="textx",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["himok.pk@gmail.com"],
    )
    message.mixed_subtype = 'related'
    body_html = """
    X<b>D</b>
    """
    message.attach_alternative(body_html, "text/html")
    #message.attach(logo_data())

    message.send(fail_silently=False)
