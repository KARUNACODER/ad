# Generated by Django 4.1.7 on 2023-03-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stat', '0005_fdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindetail',
            name='name',
            field=models.CharField(db_column='Name', max_length=20),
        ),
    ]
