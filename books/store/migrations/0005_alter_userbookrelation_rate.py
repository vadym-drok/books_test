# Generated by Django 3.2.7 on 2021-10-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_userbookrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'OK'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')]),
        ),
    ]
