# Generated by Django 3.2.7 on 2021-10-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Vadym', max_length=255),
            preserve_default=False,
        ),
    ]