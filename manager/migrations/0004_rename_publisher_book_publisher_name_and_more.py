# Generated by Django 4.0.2 on 2022-06-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_book_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='publisher_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='subject',
            new_name='subject_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='title_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
