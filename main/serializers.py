from rest_framework import serializers
from .models import *

class PlanSerializer(serializers.Serializer):
    class Meta:
        model = Plan
        fields = "__all__"
