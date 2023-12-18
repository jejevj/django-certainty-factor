# Generated by Django 4.2.6 on 2023-12-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depresi_app', '0012_userpasien_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpasien',
            name='cf',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userpasien',
            name='kode_pasien',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userpasien',
            name='kode_gejala',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userpasien',
            name='p1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userpasien',
            name='p2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userpasien',
            name='p3',
            field=models.CharField(default='', max_length=100),
        ),
    ]