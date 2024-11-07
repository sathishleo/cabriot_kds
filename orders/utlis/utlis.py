class order_class:
    def get_orderserlizer(self,orders_in_current_shift):
        menu_data = [
            {
                "client": order.client.name,
                "meal_type": order.meal_type,
                "status": order.order_status,
                "order_number": order.order_number,
                "count": order.total_pax_quantity,
                "order_items": [
                    {
                       "quantity":item.quantity,"quantity_type": item.quantity_type, "item_name":item.item.item_name
                    }
                    for item in order.order_items.all()
                ]
            }
            for order in orders_in_current_shift
        ]

        return menu_data
