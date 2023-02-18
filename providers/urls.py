from django.urls import path, include
from rest_framework.routers import SimpleRouter

from providers.views import CompanyViewSet

company_router = SimpleRouter()
company_router.register('company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(company_router.urls)),
]

