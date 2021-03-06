# Generated by Django 2.0.5 on 2018-07-10 10:30

from django.db import migrations, transaction
from fleio.billing.settings import ProductType
from fleio.billing.settings import PublicStatuses
from fleio.billing.settings import ProductAutoSetup


def change_auto_create_openstack_option(apps, schema_editor):
    config_model = apps.get_model('conf', 'Configuration')
    product_model = apps.get_model('billing', 'Product')
    product_cycle_model = apps.get_model('billing', 'ProductCycle')
    with transaction.atomic():
        for config in config_model.objects.all():
            # Enable or disable auto service creation based on previous values
            opt = config.option_set.filter(section='OPENSTACK', field='auto_create_service').first()
            auto_create = 'true' if opt is None else opt.value
            config.option_set.update_or_create(configuration=config,
                                               section='BILLING',
                                               field='auto_create_order',
                                               defaults={'value': auto_create})
            # Set the product id for the auto order creation
            opt = config.option_set.filter(section='OPENSTACK', field='product_id').first()
            if opt is None:
                auto_service = product_model.objects.filter(product_type=ProductType.openstack).first()
                if auto_service is not None:
                    auto_service_id = auto_service.id
                else:
                    auto_service_id = None
            else:
                auto_service = product_model.objects.filter(product_type=ProductType.openstack,
                                                            id=opt.value).first()
                if auto_service is not None:
                    auto_service_id = opt.value
                else:
                    auto_service_id = None

            # Change the default OpenStack product to private and auto setup to true
            if auto_service is not None:
                auto_service.status = PublicStatuses.private
                auto_service.auto_setup = ProductAutoSetup.on_order
                auto_service.save(update_fields=['status', 'auto_setup'])

            if auto_service_id is None and auto_create == 'true':
                # Disable auto create if previouselly enabled
                config.option_set.update_or_create(configuration=config,
                                                   section='BILLING',
                                                   field='auto_create_order',
                                                   defaults={'value': 'false'})
            else:
                config.option_set.update_or_create(configuration=config,
                                                   section='BILLING',
                                                   field='auto_order_service',
                                                   defaults={'value': auto_service_id})

                # Set the service cycle for auto order creation, disable auto is cycle does not exist
                opt = config.option_set.filter(section='OPENSTACK', field='product_cycle_id').first()
                if opt is None:
                    auto_service_cycle = product_cycle_model.objects.filter(product_id=auto_service_id).first()
                    if auto_service_cycle is not None:
                        auto_service_cycle_id = auto_service_cycle.id
                    else:
                        auto_service_cycle_id = None
                else:
                    auto_service_cycle_id = opt.value

                if auto_service_cycle_id is None and auto_create == 'true':
                    # Disable auto create if previouselly enabled
                    config.option_set.update_or_create(configuration=config,
                                                       section='BILLING',
                                                       field='auto_create_order',
                                                       defaults={'value': 'false'})
                else:
                    config.option_set.update_or_create(configuration=config,
                                                       section='BILLING',
                                                       field='auto_order_service_cycle',
                                                       defaults={'value': auto_service_cycle_id})

            config.option_set.filter(section='OPENSTACK', field__in=('auto_create_service',
                                                                     'product_id',
                                                                     'product_cycle_id',
                                                                     'product_name')).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0002_project_service'),
        ('core', '0003_create_default_configuration'),
    ]

    operations = [
        migrations.RunPython(change_auto_create_openstack_option),
    ]
