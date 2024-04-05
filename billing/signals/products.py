from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from billing.models import Product, Bill


@receiver(
    post_save,
    sender=Bill,
    dispatch_uid="update_total_units_sold",
)
def update_product_quantity(sender, instance: Bill, created, raw, **kwargs):
    if raw:
        return
    if not created:
        return
    for order in instance.orders:
        product = Product.objects.get(external_id=order['product'].get('external_id'))
        product.total_units_sold += order['quantity']
        product.save()
