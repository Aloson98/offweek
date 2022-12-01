# Generated by Django 4.1.3 on 2022-12-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('HEALTH', 'HEALTH'), ('EDUCATION', 'EDUCATION')], max_length=80)),
                ('content', models.TextField()),
            ],
        ),
    ]
