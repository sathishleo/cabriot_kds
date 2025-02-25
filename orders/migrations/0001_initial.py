# Generated by Django 4.2.16 on 2024-11-05 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0012_alter_dailydisplaymenuitem_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('order_status', models.CharField(choices=[('Cooking', 'Cooking'), ('Ready', 'Ready'), ('Dispatched', 'Dispatched')], max_length=10)),
                ('order_number', models.CharField(editable=False, max_length=20, unique=True)),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Tea & Snacks', 'Tea & Snacks'), ('Dinner', 'Dinner')], max_length=15)),
                ('total_pax_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('quantity_type', models.CharField(choices=[('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Numbers', 'Numbers')], max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
            ],
        ),
    ]
