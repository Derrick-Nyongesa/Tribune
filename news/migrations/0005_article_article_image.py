# Generated by Django 3.2.2 on 2021-05-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_pub_time_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='articles/'),
        ),
    ]
