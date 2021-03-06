# Generated by Django 2.1 on 2018-09-10 12:43

from django.db import migrations, models
import django.db.models.deletion
import fleio.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenStackBackupLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenStackBackupSchedule',
            fields=[
                ('id', models.BigIntegerField(default=fleio.core.utils.RandomId('osbackup.OpenStackBackupSchedule'), primary_key=True, serialize=False, unique=True)),
                ('backup_name', models.CharField(max_length=60)),
                ('backup_type', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], max_length=10)),
                ('rotation', models.IntegerField()),
                ('run_at', models.DateTimeField()),
                ('instance', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='os_backup_schedules', to='openstack.Instance')),
            ],
        ),
    ]
