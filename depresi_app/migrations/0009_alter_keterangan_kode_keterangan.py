# Generated by Django 4.2.5 on 2023-11-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depresi_app', '0008_alter_keterangan_kode_keterangan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keterangan',
            name='kode_keterangan',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
