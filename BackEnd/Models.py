# subscriptions/models.py
from django.db import models
from dateutil.relativedelta import relativedelta  # For date calculations

class Subscription(models.Model):
    BILLING_CHOICES = [("monthly", "Monthly"), ("annual", "Annual")]
    name = models.CharField(max_length=200)  # Service name (e.g., Netflix)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price in SAR
    billing_cycle = models.CharField(max_length=10, choices=BILLING_CHOICES)
    start_date = models.DateField(auto_now_add=True)  # Auto-set to today on creation
    renewal_date = models.DateField()  # Calculated based on billing cycle

    def save(self, *args, **kwargs):
        # Calculate renewal_date ONLY during initial creation (not on updates)
        if not self.pk:
            delta = relativedelta(months=1) if self.billing_cycle == "monthly" else relativedelta(years=1)
            self.renewal_date = self.start_date + delta
        super().save(*args, **kwargs)

class PriceHistory(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="price_history")
    old_price = models.DecimalField(max_digits=10, decimal_places=2)  # Track previous price
    new_price = models.DecimalField(max_digits=10, decimal_places=2)  # Track updated price
    changed_at = models.DateTimeField(auto_now_add=True)  # Timestamp of change