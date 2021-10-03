# Generated by Django 3.2.7 on 2021-10-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211003_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'OK'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]
