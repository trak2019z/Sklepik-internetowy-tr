# Generated by Django 2.1.3 on 2019-01-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SklepInternetowy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y\\%m\\%d'),
        ),
    ]