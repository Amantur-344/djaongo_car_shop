# Generated by Django 3.2.6 on 2021-08-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('engine', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(default='car.png', upload_to='cars')),
                ('release_auto', models.DateTimeField()),
                ('color', models.CharField(max_length=50)),
                ('transmission', models.BooleanField(default=True)),
                ('rul', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
