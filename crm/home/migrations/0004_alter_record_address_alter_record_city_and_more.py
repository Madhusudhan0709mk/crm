# Generated by Django 5.0.1 on 2024-01-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.CharField(max_length=50),
        ),
    ]
