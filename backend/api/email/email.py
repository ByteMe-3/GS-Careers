import os
from email.mime.image import MIMEImage

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

path = os.path.join(settings.BASE_DIR, "api", "email/")


def attach_image(message, file_name):
    image_path = os.path.join(path, "images/")
    background_path = image_path + file_name
    attachment = open(background_path, "rb")

    image = MIMEImage(attachment.read())
    image.add_header("Content-ID", "<{}>".format(file_name))
    message.attach(image)


def send_points_email():
    message = EmailMultiAlternatives(
        subject="Points changed",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["himok.pk@gmail.com"],
    )
    message.mixed_subtype = "related"

    with open(path + "points.html") as f:
        body_html = f.read()
        message.attach_alternative(body_html, "text/html")

    attach_image(message, "background.jpg")

    attach_image(message, "logo.png")
    attach_image(message, "logo-dark.png")
    attach_image(message, "hero_shadow.jpg")
    attach_image(message, "pull-quote.jpg")

    attach_image(message, "footer_ico_instagram.jpg")
    attach_image(message, "footer_ico_twitter.jpg")
    attach_image(message, "footer_ico_linkedin.jpg")
    attach_image(message, "footer_ico_youtube.jpg")

    message.send(fail_silently=False)


def send_event_email():
    message = EmailMultiAlternatives(
        subject="Event alert",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["himok.pk@gmail.com"],
    )
    message.mixed_subtype = "related"

    with open(path + "event-mail.html") as f:
        body_html = f.read()
        message.attach_alternative(body_html, "text/html")

    attach_image(message, "background.jpg")

    attach_image(message, "logo.png")
    attach_image(message, "logo-dark.png")
    attach_image(message, "hero_shadow.jpg")
    attach_image(message, "pull-quote.jpg")

    attach_image(message, "footer_ico_instagram.jpg")
    attach_image(message, "footer_ico_twitter.jpg")
    attach_image(message, "footer_ico_linkedin.jpg")
    attach_image(message, "footer_ico_youtube.jpg")

    message.send(fail_silently=False)


def send_activation_email():
    message = EmailMultiAlternatives(
        subject="Active your account",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["himok.pk@gmail.com"],
    )
    message.mixed_subtype = "related"

    with open(path + "activation.html") as f:
        body_html = f.read()
        message.attach_alternative(body_html, "text/html")

    attach_image(message, "background.jpg")

    attach_image(message, "footer_ico_instagram.jpg")
    attach_image(message, "footer_ico_twitter.jpg")
    attach_image(message, "footer_ico_linkedin.jpg")
    attach_image(message, "footer_ico_youtube.jpg")

    message.send(fail_silently=False)
