# Generated by Django 2.1 on 2018-10-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_auto_20181002_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='companies',
            field=models.ManyToManyField(blank=True, related_name='articles', to='analysis.Company'),
        ),
    ]
