# Generated by Django 5.0.6 on 2024-07-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorsbooks', '0004_rename_name_author_first_name_author_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
