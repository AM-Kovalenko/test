# Generated by Django 4.0 on 2021-12-22 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_creditapplication_product_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditapplication',
            name='product_list',
            field=models.ManyToManyField(related_name='credit_applications', to='task.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='task.manufacturer'),
        ),
    ]
