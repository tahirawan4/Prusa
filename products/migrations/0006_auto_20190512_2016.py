# Generated by Django 2.2 on 2019-05-12 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_customcontent_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('accessory', 'Accessory'), ('product', 'Product')], default='product', max_length=100),
        ),
    ]
