# Generated by Django 4.2.5 on 2023-12-31 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoAPP', '0002_alter_principal_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('subject', models.CharField(max_length=20)),
                ('attendance', models.CharField(max_length=20)),
            ],
        ),
    ]
