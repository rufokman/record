# Generated by Django 3.2.16 on 2022-10-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancingapp', '0004_card_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='passport',
            field=models.FileField(default='', upload_to='passports/', verbose_name='Паспорт'),
        ),
    ]