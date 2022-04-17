# Generated by Django 4.0.3 on 2022-04-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moja_strona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.GenericIPAddressField()),
                ('delivery', models.IntegerField(choices=[('-1', 'select'), ('0', 'courier'), ('1', 'parcel machine'), ('2', 'pick up in person')])),
                ('description', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
