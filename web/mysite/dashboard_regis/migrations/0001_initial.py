# Generated by Django 3.2.13 on 2022-06-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCustomer', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('phoneNumber', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
