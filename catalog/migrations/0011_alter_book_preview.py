# Generated by Django 3.2.15 on 2022-10-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_book_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='preview',
            field=models.FileField(null=True, upload_to='covers/'),
        ),
    ]
