# Generated by Django 2.2 on 2020-03-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200302_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published date'),
        ),
    ]
