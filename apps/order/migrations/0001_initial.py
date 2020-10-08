# Generated by Django 3.1.1 on 2020-10-08 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('cash_received', models.DecimalField(decimal_places=2, max_digits=9)),
                ('change', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
