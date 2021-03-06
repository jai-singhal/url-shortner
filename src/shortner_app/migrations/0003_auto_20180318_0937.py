# Generated by Django 2.0.3 on 2018-03-18 09:37

from django.db import migrations, models
import shortner_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner_app', '0002_auto_20180318_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='url',
            field=models.CharField(max_length=220, unique=True, validators=[shortner_app.validators.validataURL]),
        ),
    ]
