# Generated by Django 4.0.3 on 2022-04-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moja_strona', '0008_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('-1', 'courier'), ('0', 'parcel machine'), ('1', 'pick up in person')], max_length=64),
        ),
    ]
