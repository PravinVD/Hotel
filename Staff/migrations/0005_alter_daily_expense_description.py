# Generated by Django 4.2 on 2023-04-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0004_daily_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_expense',
            name='description',
            field=models.TextField(),
        ),
    ]
