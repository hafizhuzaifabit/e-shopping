from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Populates the database with sample products'

    def handle(self, *args, **options):
        products_data = [
            {'name': 'Laptop Pro 15', 'description': 'High-performance laptop with 16GB RAM', 'price': 1299.99, 'stock': 10, 'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&h=400&fit=crop'},
            {'name': 'Wireless Mouse', 'description': 'Ergonomic wireless mouse', 'price': 29.99, 'stock': 50, 'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=400&h=400&fit=crop'},
            {'name': 'Mechanical Keyboard', 'description': 'RGB mechanical keyboard', 'price': 89.99, 'stock': 25, 'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&h=400&fit=crop'},
            {'name': '4K Monitor', 'description': '27-inch 4K UHD monitor', 'price': 399.99, 'stock': 15, 'image_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400&h=400&fit=crop'},
            {'name': 'USB-C Hub', 'description': '7-in-1 USB-C hub', 'price': 49.99, 'stock': 30, 'image_url': 'https://images.unsplash.com/photo-1625842268584-8f3296236761?w=400&h=400&fit=crop'},
            {'name': 'Webcam HD', 'description': '1080p HD webcam', 'price': 79.99, 'stock': 20, 'image_url': 'https://images.unsplash.com/photo-1587825147138-733719c10a57?w=400&h=400&fit=crop'},
            {'name': 'Noise Cancelling Headphones', 'description': 'Premium wireless headphones', 'price': 199.99, 'stock': 12, 'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop'},
            {'name': 'External SSD 1TB', 'description': 'Fast portable SSD drive', 'price': 129.99, 'stock': 18, 'image_url': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=400&h=400&fit=crop'},
            {'name': 'Standing Desk', 'description': 'Adjustable height desk', 'price': 299.99, 'stock': 8, 'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&h=400&fit=crop'},
            {'name': 'Desk Lamp', 'description': 'LED desk lamp with dimmer', 'price': 39.99, 'stock': 40, 'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400&h=400&fit=crop'},
            {'name': 'Laptop Stand', 'description': 'Aluminum laptop stand', 'price': 34.99, 'stock': 22, 'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400&h=400&fit=crop'},
            {'name': 'Cable Organizer', 'description': 'Cable management kit', 'price': 14.99, 'stock': 60, 'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=400&fit=crop'},
            {'name': 'Wireless Charger', 'description': 'Fast wireless charging pad', 'price': 24.99, 'stock': 35, 'image_url': 'https://images.unsplash.com/photo-1609091839311-d5365f6ff4e0?w=400&h=400&fit=crop'},
            {'name': 'Bluetooth Speaker', 'description': 'Portable Bluetooth speaker', 'price': 59.99, 'stock': 28, 'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400&h=400&fit=crop'},
            {'name': 'Tablet 10 inch', 'description': '10-inch Android tablet', 'price': 249.99, 'stock': 5, 'image_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400&h=400&fit=crop'},
            {'name': 'Smart Watch', 'description': 'Fitness tracking smartwatch', 'price': 179.99, 'stock': 0, 'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop'},  # Out of stock
            {'name': 'Phone Case', 'description': 'Protective phone case', 'price': 19.99, 'stock': 100, 'image_url': 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=400&fit=crop'},
            {'name': 'Screen Protector', 'description': 'Tempered glass screen protector', 'price': 12.99, 'stock': 75, 'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=400&fit=crop'},
        ]

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'image_url': product_data.get('image_url', '')
                }
            )
            # Update image_url if product exists but doesn't have one
            if not created and not product.image_url and product_data.get('image_url'):
                product.image_url = product_data['image_url']
                product.save()
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new products!')
        )

