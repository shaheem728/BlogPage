# Generated by Django 5.0.6 on 2024-06-12 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]
