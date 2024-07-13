# Generated by Django 5.0.6 on 2024-07-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorsbooks', '0003_alter_book_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]