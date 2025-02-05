from products.models import Category, Tag, Product

# Create 5 categories
categories = [
    'Electronics',
    'Clothing',
    'Books',
    'Home Appliances',
    'Toys'
]

for category_name in categories:
    Category.objects.create(name=category_name)

# Create 10 tags
tags = [
    'New',
    'Sale',
    'Popular',
    'Limited Edition',
    'Trending',
    'Discounted',
    'Exclusive',
    'Gift',
    'Featured',
    'Top Rated'
]

for tag_name in tags:
    Tag.objects.create(name=tag_name)

# Create 20 products
product_data = [
    ("Laptop", "A high-end laptop", 1200.00, "Electronics", ["New", "Popular"]),
    ("T-Shirt", "A stylish t-shirt", 20.00, "Clothing", ["Sale", "Trending"]),
    ("Novel", "An interesting novel", 15.00, "Books", ["New", "Discounted"]),
    ("Blender", "A powerful kitchen blender", 100.00, "Home Appliances", ["Exclusive"]),
    ("Toy Car", "A remote-controlled toy car", 25.00, "Toys", ["Gift"]),
    ("Smartphone", "Latest smartphone with high-end features", 999.00, "Electronics", ["New", "Trending"]),
    ("Jeans", "Comfortable and stylish jeans", 40.00, "Clothing", ["Popular", "Discounted"]),
    ("Cookbook", "A collection of delicious recipes", 25.00, "Books", ["Featured"]),
    ("Microwave", "A compact microwave oven", 60.00, "Home Appliances", ["Sale"]),
    ("Doll", "A cute and collectible doll", 30.00, "Toys", ["Top Rated"]),
    ("Camera", "A professional camera", 500.00, "Electronics", ["New", "Exclusive"]),
    ("Sweater", "A warm sweater for the winter", 50.00, "Clothing", ["Gift"]),
    ("Magazine", "A monthly fashion magazine", 10.00, "Books", ["Trending"]),
    ("Washing Machine", "A washing machine with advanced features", 350.00, "Home Appliances", ["Popular"]),
    ("Puzzle", "A 1000-piece puzzle", 20.00, "Toys", ["New", "Exclusive"]),
    ("Monitor", "A 27-inch high-definition monitor", 250.00, "Electronics", ["Discounted"]),
    ("Jacket", "A leather jacket for all seasons", 150.00, "Clothing", ["Limited Edition"]),
    ("Dictionary", "An English dictionary for learners", 12.00, "Books", ["Top Rated"]),
    ("Air Conditioner", "A compact air conditioner", 400.00, "Home Appliances", ["Exclusive"]),
    ("Train Set", "A model train set", 80.00, "Toys", ["Gift", "Trending"])
]

for name, description, price, category_name, tag_names in product_data:
    # Get or create the category
    category = Category.objects.get(name=category_name)
    
    # Create the product
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        category=category
    )
    
    # Add tags to the product
    for tag_name in tag_names:
        tag = Tag.objects.get(name=tag_name)
        product.tags.add(tag)
    
    # Save the product after adding tags
    product.save()

print("Database populated with categories, tags, and products!")
