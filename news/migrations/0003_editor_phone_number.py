# Generated by Django 3.2.2 on 2021-05-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
