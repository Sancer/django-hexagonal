# Generated by Django 4.1.7 on 2023-04-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deleted date'),
        ),
    ]
