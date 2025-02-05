"""
The routercreates the API endpoints for the Category, Tag, and Product viewsets.
Endpoints provided:
    - /api/categories/ : CRUD operations for Category instances.
    - /api/tags/       : CRUD operations for Tag instances.
    - /api/products/   : CRUD operations for Product instances, including support for filtering.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
