# Generated by Django 2.0.3 on 2018-03-23 16:33

from django.db import migrations, models
import shortner_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner_app', '0005_auto_20180318_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='url',
            field=models.TextField(unique=True, validators=[shortner_app.validators.validataURL]),
        ),
    ]
