# Generated by Django 2.2.7 on 2019-11-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20191118_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='Book_Covers/'),
        ),
    ]
