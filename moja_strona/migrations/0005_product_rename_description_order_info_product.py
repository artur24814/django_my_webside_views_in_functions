# Generated by Django 4.0.3 on 2022-04-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moja_strona', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='description',
            new_name='info_product',
        ),
    ]
