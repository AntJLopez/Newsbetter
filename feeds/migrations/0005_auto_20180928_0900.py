# Generated by Django 2.1 on 2018-09-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20180925_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.URLField(max_length=500),
        ),
    ]
