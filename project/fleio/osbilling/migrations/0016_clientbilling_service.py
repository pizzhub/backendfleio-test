# Generated by Django 2.2.5 on 2019-10-14 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0020_product_hide_services'),
        ('osbilling', '0015_pricingplan_reseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientbilling',
            name='service',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_billing', to='billing.Service'),
        ),
    ]
