# Generated by Django 2.2.3 on 2019-07-17 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0024_cluster_clustertemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolumeSnapshot',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=32)),
                ('progress', models.IntegerField(null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('size', models.IntegerField()),
                ('metadata', models.CharField(blank=True, max_length=1024, null=True)),
                ('sync_version', models.BigIntegerField(default=0)),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openstack.Project', to_field='project_id')),
                ('region', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openstack.OpenstackRegion')),
                ('volume', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openstack.Volume')),
            ],
        ),
    ]
