# subscriptions/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscription, PriceHistory

@receiver(post_save, sender=Subscription)
def track_price_change(sender, instance, **kwargs):
    # Skip on creation (only trigger on updates)
    if not kwargs.get("created"):
        try:
            old_sub = Subscription.objects.get(pk=instance.pk)
            if old_sub.price != instance.price:  # Check if price changed
                PriceHistory.objects.create(
                    subscription=instance,
                    old_price=old_sub.price,
                    new_price=instance.price
                )
        except Subscription.DoesNotExist:
            pass  # Handle edge case (unlikely in normal flow)