# Generated by Django 4.2.5 on 2023-11-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depresi_app', '0004_alter_keterangan_kode_keterangan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keterangan',
            name='kode_keterangan',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, unique=True),
        ),
    ]
