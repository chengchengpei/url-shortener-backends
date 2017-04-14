from api.models import Link
from rest_framework import serializers

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('long_url', 'short_url', 'created', 'visit_count')
