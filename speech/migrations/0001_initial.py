# Generated by Django 4.2.1 on 2023-05-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Default Author', max_length=100)),
                ('text', models.CharField(default='NO TEXT', max_length=200)),
            ],
        ),
    ]
