# Generated by Django 4.1.7 on 2023-03-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindetail',
            name='dept',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
