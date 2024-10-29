from django import template

register = template.Library()

@register.filter
def format_quantity(item):
    """Custom filter to format item quantities based on their type."""
    if item.quantity_type == "Numbers":
        # Show as 1 decimal place if it's a float, otherwise as an integer
        return f"{item.quantity:.1f} Numbers" if item.quantity % 1 != 0 else f"{int(item.quantity)} Numbers"
    elif item.quantity_type == "Kilograms":
        # Show with leading zero if less than 10 and one decimal
        return f"{item.quantity:04.1f} Kilograms"
    elif item.quantity_type == "Grams":
        # Show with leading zeros for grams
        return f"{int(item.quantity):03d} Grams"
    else:
        # Default: show with 2 decimal places for other quantity types
        return f"{item.quantity:.2f} {item.quantity_type}"



@register.filter
def grams_to_kilograms(value):
    if value is not None:
        return value / 1000  # Convert grams to kilograms
    return value

@register.filter
def divide_by_100(value):
    if value is not None:
        return value / 100  # Divide by 100
    return value
