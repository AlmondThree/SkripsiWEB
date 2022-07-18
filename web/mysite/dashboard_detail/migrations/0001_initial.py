# Generated by Django 3.2.13 on 2022-06-11 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard_regis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('limit', models.IntegerField()),
                ('usage', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('idCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard_regis.datacustomer')),
            ],
        ),
    ]