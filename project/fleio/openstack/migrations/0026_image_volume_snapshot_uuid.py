# Generated by Django 2.2.3 on 2019-07-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0025_volumesnapshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='volume_snapshot_uuid',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
