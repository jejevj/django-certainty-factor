# Generated by Django 4.2.5 on 2023-11-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depresi_app', '0005_alter_keterangan_kode_keterangan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keterangan',
            name='kode_keterangan',
            field=models.CharField(auto_created=True, max_length=3, primary_key=True, serialize=False, unique=True),
        ),
    ]
