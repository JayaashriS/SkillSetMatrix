# Generated by Django 4.1.7 on 2023-04-26 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillsmatrix',
            old_name='skill',
            new_name='Skills_Name',
        ),
    ]
