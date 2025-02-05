"""
This module defines the API endpoints for managing Categories, Tags, and Products using Django REST Framework.

Classes:
    - CategoryViewSet: Provides a complete CRUD interface for Category instances.
    - TagViewSet: Provides a complete CRUD interface for Tag instances.
    - ProductFilter: Defines filtering options for Product instances.
    - ProductViewSet: Provides a complete CRUD interface for Product instances with dynamic filtering support.

Filtering:
    The ProductViewSet supports filtering using both django_filters via the defined ProductFilter class and 
    an override of get_queryset to apply additional query parameter filters:
        - name: Case-insensitive partial match on the product's name.
        - category: Case-insensitive partial match on the product's associated category name.
        - tags: Case-insensitive partial match on the product's associated tags.
"""

from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Category, Tag, Product
from .serializers import CategorySerializer, TagSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.

    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.

    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProductFilter(filters.FilterSet):
    """
    FilterSet for filtering Product instances based on specific criteria.

    Filters:
        - name: Filters products whose name contains the provided substring (case-insensitive).
        - category: Filters products based on a partial match of the related category's name (case-insensitive).
        - tags: Filters products based on a partial match of the names of associated tags (case-insensitive).
    """
    name = filters.CharFilter(lookup_expr='icontains', required=False)
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains', required=False)
    tags = filters.CharFilter(field_name='tags__name', lookup_expr='icontains', required=False)

    class Meta:
        model = Product
        fields = ['name', 'category', 'tags']

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed with filtering.

    This viewset uses django_filters to filter products based on 'name', 'category', and 'tags'.
    Additionally, the `get_queryset` method is overridden to support dynamic filtering based on
    query parameters passed in the request.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        """
        Optionally restricts the returned products by filtering against
        query parameters in the URL.

        Query Parameters:
            - name: Case-insensitive partial match on the product name.
            - category: Case-insensitive partial match on the category name.
            - tags: Case-insensitive partial match on the tag names.

        Returns:
            A QuerySet of filtered Product instances.
        """
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        tags = self.request.query_params.get('tags', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if tags:
            queryset = queryset.filter(tags__name__icontains=tags)
        return queryset
