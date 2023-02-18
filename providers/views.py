from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from providers.filter import CompanyFilter
from providers.models import Company
from providers.permissions import ActiveUsers
from providers.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter
    permission_classes = ActiveUsers

    serializer_class = CompanySerializer
