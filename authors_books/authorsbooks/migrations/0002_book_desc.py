# Generated by Django 5.0.6 on 2024-07-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorsbooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
