# Generated by Django 3.2.3 on 2021-09-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20210701_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('ECE', 'Electronics and communication'), ('MECH', 'Mechanical')], max_length=10),
        ),
    ]
