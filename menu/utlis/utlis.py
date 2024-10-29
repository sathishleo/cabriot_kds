class Displaysection:
    VEGETABLE = 'vegetable'
    MAIN = 'main'
    BREAD = 'bread'
    key_vegetable="VEGETABLE"
    key_main="MAIN"
    key_bread="BREAD"

    def get_displaysection(self,section):
        if Displaysection.VEGETABLE == section:
            return Displaysection.key_vegetable
        elif Displaysection.MAIN == section:
            return Displaysection.key_main
        elif Displaysection.BREAD == section:
            return Displaysection.key_bread
        else:
            return " "

    def quantitytype_format(self, menu):
        formatted_menu = []  # Initialize an empty list to hold formatted items
        for obj in menu:
            if obj.quantity_type == "Grams":
                # Format for grams
                formatted_quantity = f"{int(obj.quantity):03d} Grams"  # Format with leading zeros for whole numbers
            elif obj.quantity_type == "Kilograms":
                # Format for kilograms
                formatted_quantity = f"{obj.quantity:.2f} Kilograms"  # Format to 2 decimal places
            elif obj.quantity_type == "Numbers":
                # Format for numbers
                formatted_quantity = f"{obj.quantity:.2f} Numbers"  # Format to 2 decimal places
            else:
                # Default case (you can add more types as needed)
                formatted_quantity = f"{obj.quantity} {obj.quantity_type}"

            # Append the formatted string to the formatted_menu list
            formatted_menu.append(formatted_quantity)

        return formatted_menu

    def get_formatted_menu_items(self,menu_items):
        # menu_items = MenuItem.objects.all()  # Retrieve all menu items
        formatted_items = []

        for item in menu_items:
            if item.quantity_type == "Grams":
                formatted_quantity = f"{int(item.quantity):03d} Grams"  # 3-digit format for grams
            elif item.quantity_type == "Kilograms":
                formatted_quantity = f"{item.quantity:.2f} Kilograms"  # 2 decimal places for kilograms
            elif item.quantity_type == "Numbers":
                formatted_quantity = int(item.quantity)
            else:
                formatted_quantity = f"{item.quantity}"  # Default format

            formatted_items.append({
                'quantity': formatted_quantity,  # Add formatted quantity
                'quantity_type': item.quantity_type
            })

        return formatted_items
