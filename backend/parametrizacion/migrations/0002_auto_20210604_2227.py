# Generated by Django 3.1.7 on 2021-06-04 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametrizacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametrizacion',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametrizacion',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]