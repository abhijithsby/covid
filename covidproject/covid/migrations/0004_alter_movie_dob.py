# Generated by Django 3.2.7 on 2021-10-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_auto_20211010_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='DOB',
            field=models.DateField(),
        ),
    ]