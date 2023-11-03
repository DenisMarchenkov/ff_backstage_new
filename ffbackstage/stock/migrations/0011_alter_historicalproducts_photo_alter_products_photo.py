# Generated by Django 4.2.4 on 2023-11-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_historicalproducts_photo_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproducts',
            name='photo',
            field=models.TextField(blank=True, default='product_photos/skincare_icon.png', max_length=100, null=True, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, default='product_photos/skincare_icon.png', null=True, upload_to='product_photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
