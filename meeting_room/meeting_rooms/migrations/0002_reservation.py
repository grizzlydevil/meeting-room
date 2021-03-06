# Generated by Django 3.2.7 on 2021-10-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20211004_1358'),
        ('meeting_rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('employee', models.ManyToManyField(to='employee.Employee')),
                ('meeting_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting_rooms.room')),
            ],
        ),
    ]
