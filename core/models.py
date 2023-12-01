import os
from django.db import models


class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField("Request Date", auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ["-timestamp", "email"]


class Contact(models.Model):
    CONTACT_CHOICES = (
        ("email", "Email"),
        ("phone", "Phone"),
        ("whatsapp", "Whatsapp"),
        ("telegram", "Telegram"),
    )

    name = models.CharField(max_length=10, choices=CONTACT_CHOICES)

    ICON_CHOICES = (
        ("/images/contact/email.svg", "Email"),
        ("/images/contact/phone.svg", "Phone"),
        ("/images/contact/whatsapp.svg", "Whatsapp"),
        ("/images/contact/telegram.svg", "Telegram"),
    )

    icon = models.CharField(max_length=255, choices=ICON_CHOICES)
    link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name