# Generated by Django 3.0.7 on 2020-06-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_item_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='https://cdn.hipwallpaper.com/i/83/43/NEbSx4.jpg', upload_to=''),
        ),
    ]