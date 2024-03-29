# Generated by Django 3.2.13 on 2022-05-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0002_auto_20220505_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField(max_length=50)),
                ('customer_description', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='data',
            name='nama_pelanggan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.customerid'),
        ),
    ]
