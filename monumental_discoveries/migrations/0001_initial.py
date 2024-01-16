# Generated by Django 4.2.9 on 2024-01-15 17:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('guide_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.BigIntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=20)),
                ('show_booking', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuideBooking',
            fields=[
                ('guide_booking_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('booking_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('success', 'Success'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=30)),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.guide')),
            ],
        ),
        migrations.CreateModel(
            name='Monuments',
            fields=[
                ('monuments_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('monuments_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='monuments_images/')),
                ('monument_location', models.CharField(max_length=256)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketBooking',
            fields=[
                ('ticket_booking_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('booking_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('number_of_person', models.IntegerField()),
                ('status', models.CharField(choices=[('success', 'Success'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=30)),
                ('monuments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.monuments')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_receipt', models.CharField(max_length=256)),
                ('payment_status', models.CharField(choices=[('success', 'Success'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=30)),
                ('guide_booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.guidebooking')),
                ('ticket_booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.ticketbooking')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.user')),
            ],
        ),
        migrations.AddField(
            model_name='monuments',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.state'),
        ),
        migrations.AddField(
            model_name='guidebooking',
            name='monuments_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.monuments'),
        ),
        migrations.AddField(
            model_name='guidebooking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.user'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('rating', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('complain_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.guide')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.user')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.state'),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('audio_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('audio_file', models.FileField(upload_to='monuments_audio/')),
                ('audio_language', models.CharField(choices=[('hindi', 'Hindi'), ('english', 'English'), ('gujarati', 'Gujarati')], max_length=30)),
                ('monuments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monumental_discoveries.monuments')),
            ],
        ),
    ]