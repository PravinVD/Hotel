# Generated by Django 4.2 on 2023-04-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Table_number', models.IntegerField()),
                ('Number_Of_Person', models.IntegerField()),
                ('item0', models.CharField(max_length=300)),
                ('item_rate0', models.IntegerField(null=True)),
                ('item_qty0', models.IntegerField(default=0)),
                ('item_total0', models.IntegerField(null=True)),
                ('item1', models.CharField(max_length=300)),
                ('item_rate1', models.IntegerField(null=True)),
                ('item_qty1', models.IntegerField(default=0)),
                ('item_total1', models.IntegerField(null=True)),
                ('item2', models.CharField(max_length=300)),
                ('item_rate2', models.IntegerField(null=True)),
                ('item_qty2', models.IntegerField(default=0)),
                ('item_total2', models.IntegerField(null=True)),
                ('item3', models.CharField(max_length=300)),
                ('item_rate3', models.IntegerField(null=True)),
                ('item_qty3', models.IntegerField(default=0)),
                ('item_total3', models.IntegerField(null=True)),
                ('item4', models.CharField(max_length=300)),
                ('item_rate4', models.IntegerField(null=True)),
                ('item_qty4', models.IntegerField(default=0)),
                ('item_total4', models.IntegerField(null=True)),
                ('item5', models.CharField(max_length=300)),
                ('item_rate5', models.IntegerField(null=True)),
                ('item_qty5', models.IntegerField(default=0)),
                ('item_total5', models.IntegerField(null=True)),
                ('item6', models.CharField(max_length=300)),
                ('item_rate6', models.IntegerField(null=True)),
                ('item_qty6', models.IntegerField(default=0)),
                ('item_total6', models.IntegerField(null=True)),
                ('item7', models.CharField(max_length=300)),
                ('item_rate7', models.IntegerField(null=True)),
                ('item_qty7', models.IntegerField(default=0)),
                ('item_total7', models.IntegerField(null=True)),
                ('item8', models.CharField(max_length=300)),
                ('item_rate8', models.IntegerField(null=True)),
                ('item_qty8', models.IntegerField(default=0)),
                ('item_total8', models.IntegerField(null=True)),
                ('item9', models.CharField(max_length=300)),
                ('item_rate9', models.IntegerField(null=True)),
                ('item_qty9', models.IntegerField(default=0)),
                ('item_total9', models.IntegerField(null=True)),
                ('total', models.IntegerField()),
                ('Order_date', models.DateTimeField()),
                ('Order_Status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=30)),
            ],
        ),
    ]
