# Generated by Django 5.0.6 on 2024-06-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
