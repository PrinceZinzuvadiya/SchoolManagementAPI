# Generated by Django 4.2.5 on 2023-12-31 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InfoAPP', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='feespending',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
