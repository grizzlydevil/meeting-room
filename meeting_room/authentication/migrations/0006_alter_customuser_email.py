# Generated by Django 3.2.7 on 2021-10-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email'),
        ),
    ]