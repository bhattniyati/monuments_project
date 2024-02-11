# Generated by Django 4.2.9 on 2024-02-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monumental_discoveries', '0008_alter_monuments_monument_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='guide_id',
        ),
        migrations.RemoveField(
            model_name='guidebooking',
            name='guide_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.ImageField(null=True, upload_to='GUIDE_PHOTOS'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Guide',
        ),
    ]