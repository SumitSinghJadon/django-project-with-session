# Generated by Django 5.0.6 on 2024-05-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_notes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
