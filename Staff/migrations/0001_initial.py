# Generated by Django 4.2 on 2023-04-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Mobile_No', models.CharField(max_length=13)),
                ('Create_date', models.DateField()),
                ('Last_update_Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]