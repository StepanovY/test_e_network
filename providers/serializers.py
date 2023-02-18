from rest_framework import serializers

from providers.models import Company


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
