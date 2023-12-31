# Generated by Django 4.2.6 on 2023-11-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_contact_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='icon',
            field=models.CharField(choices=[('/images/contact/email.svg', 'Email'), ('/images/contact/phone.svg', 'Phone'), ('/images/contact/whatsapp.svg', 'Whatsapp'), ('/images/contact/telegram.svg', 'Telegram')], max_length=255),
        ),
    ]
