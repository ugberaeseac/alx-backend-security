# Generated by Django 5.2.4 on 2025-07-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_tracking', '0002_blockedip_requestlog_city_requestlog_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuspiciousIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=45)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
