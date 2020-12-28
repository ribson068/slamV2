# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-12-28 21:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('slambook', '0002_auto_20201217_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('isread', models.BooleanField(default=False)),
                ('hyperlink', models.TextField(blank=True)),
                ('fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nfr', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Of_Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_notif', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='typeofNotification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NtypNotif', to='slambook.Type_Of_Notification'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
