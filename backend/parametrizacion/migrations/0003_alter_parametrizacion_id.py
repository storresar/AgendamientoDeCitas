# Generated by Django 3.2.4 on 2021-06-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametrizacion', '0002_auto_20210604_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametrizacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
