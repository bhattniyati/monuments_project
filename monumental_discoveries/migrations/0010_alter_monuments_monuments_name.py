# Generated by Django 4.2.9 on 2024-02-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monumental_discoveries', '0009_remove_complain_guide_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monuments',
            name='monuments_name',
            field=models.CharField(max_length=40),
        ),
    ]