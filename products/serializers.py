from rest_framework import serializers
from .models import Category, Tag, Product

# Serializer for the Category model.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields from the Category model.

# Serializer for the Tag model.
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'  # Include all fields from the Tag model.

# Serializer for the Product model.
# This serializer nests the CategorySerializer and TagSerializer to provide detailed
# information for the related category and tags.
class ProductSerializer(serializers.ModelSerializer):
    # Use CategorySerializer to serialize the related category field.
    category = CategorySerializer()
    
    # Use TagSerializer for each tag in the many-to-many relationship.
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the Product model.
