# Generated by Django 3.2.3 on 2021-06-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditoria', '0002_alter_auditoria_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
