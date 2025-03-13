# subscriptions/serializers.py
from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"  # Expose all fields via API

# subscriptions/views.py
from rest_framework import generics
from django.db.models import Case, When, F, DecimalField
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        # Annotate monthly/annual costs dynamically for API responses
        return Subscription.objects.annotate(
            monthly_cost=Case(
                When(billing_cycle="monthly", then=F("price")),
                When(billing_cycle="annual", then=F("price") / 12),
                output_field=DecimalField(max_digits=10, decimal_places=2),
            ),
            annual_cost=Case(
                When(billing_cycle="monthly", then=F("price") * 12),
                When(billing_cycle="annual", then=F("price")),
                output_field=DecimalField(max_digits=10, decimal_places=2),
            )
        )

class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    lookup_field = "id"  # Delete by subscription ID