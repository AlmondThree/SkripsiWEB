# Generated by Django 3.2.13 on 2022-07-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_detail', '0004_auto_20220615_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlog',
            name='id',
            field=models.BigAutoField(auto_created=True, default=int, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerlog',
            name='tanggal',
            field=models.DateField(),
        ),
        migrations.RemoveField(
            model_name='history',
            name='month',
        ),
        migrations.AddField(
            model_name='history',
            name='month',
            field=models.ManyToManyField(db_column='tanggal', to='dashboard_detail.customerLog'),
        ),
    ]
