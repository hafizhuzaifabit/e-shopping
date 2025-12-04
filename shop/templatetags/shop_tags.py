from django import template
from ..models import Product

register = template.Library()


@register.simple_tag
def total_products():
    """Custom template tag to return total number of products."""
    return Product.objects.count()


@register.filter
def format_price(value):
    """Custom filter to format prices with thousand separators."""
    try:
        # Convert to float if it's a Decimal or string
        price = float(value)
        # Format with 2 decimal places and thousand separators
        return f"{price:,.2f}"
    except (ValueError, TypeError):
        return value

