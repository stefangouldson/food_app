# Generated by Django 3.0.7 on 2020-12-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://platerate.com/images/tempfoodnotext.png', max_length=500),
        ),
    ]
