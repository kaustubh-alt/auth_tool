# Generated by Django 5.1.3 on 2024-12-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veri', '0003_customuser_usid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='usid',
            field=models.CharField(max_length=50),
        ),
    ]