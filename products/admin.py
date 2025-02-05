from django.contrib import admin
from .models import Category, Tag, Product

# Register the Category model with the admin site.
admin.site.register(Category)

# Register the Tag model with the admin site.
admin.site.register(Tag)

# Register the Product model with the admin site.
admin.site.register(Product)