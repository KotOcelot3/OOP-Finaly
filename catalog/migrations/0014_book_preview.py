# Generated by Django 3.2.15 on 2022-10-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_book_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preview',
            field=models.FileField(null=True, upload_to='pdf/'),
        ),
    ]
