from django.db import models
 # Import the existing Item model from the menu app
from django.utils import timezone
from django.core.exceptions import ValidationError
from menu.models import MenuItem


class Client(models.Model):
    name = models.CharField(max_length=100)
    client_code=models.CharField(max_length=20,null=True, blank=True)

    # Add any other client-specific fields

    def __str__(self):
        if self.client_code is None:
            return f"{self.name}"+"-"+"-"
        return f"{self.name}-{self.client_code}"

class Order(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Tea & Snacks', 'Tea & Snacks'),
        ('Dinner', 'Dinner'),
    ]

    STATUS_CHOICES = [
        ('Cooking', 'Cooking'),
        ('Ready', 'Ready'),
        ('Dispatched', 'Dispatched'),
    ]

    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='Cooking')
    order_number = models.CharField(max_length=20, unique=True, editable=False)
    meal_type = models.CharField(max_length=15, choices=MEAL_TYPES,null=True,blank=True)
    total_pax_quantity = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Call the parent save method first to ensure the instance has an ID
        super().save(*args, **kwargs)

        # Only generate order_number if it is not set
        if not self.order_number:
            date_str = timezone.now().strftime("%Y%m%d")  # e.g., "20231105"
            client_id = str(self.client.id).zfill(3)  # Pads client ID to 3 digits

            # Use the primary key (ID) for order_number
            self.order_number = f"{date_str}-{client_id}-{self.id}"

            # Now save the instance again to update the order_number
            super().save(update_fields=['order_number'])


    def __str__(self):
        return f"Order {self.order_number} - {self.meal_type} ({self.date})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # Reference to the existing Item model in menu app
    quantity = models.CharField(max_length=10, null=True, blank=True)
    quantity_type = models.CharField(max_length=20, choices=[
        ('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Numbers', 'Numbers')],null=True,blank=True)

    def __str__(self):
        return f"{self.quantity} {self.quantity_type} of {self.item.item_name} for {self.order}"

# class Workday(models.Model):
#     date = models.DateField(unique=True)
#
#     def __str__(self):
#         return f"Workday on {self.date}"
# class MealSchedule(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title

# class Mealtime(models.Model):
#     Meal= [
#         ('Breakfast', 'Breakfast'),
#         ('Lunch', 'Lunch'),
#         ('Tea & Snacks', 'Tea & Snacks'),
#         ('Dinner', 'Dinner'),
#     ]
#     meal_schedule = models.ForeignKey(MealSchedule, on_delete=models.CASCADE, related_name='mealtimes')
#     meal_name = models.CharField(max_length=20, choices=Meal)
#     check_in = models.TimeField(blank=True, null=True)
#
#     def __str__(self):
#         return self.meal_name



from django.db import models
from django.contrib.auth.models import User

# class MealTime(models.Model): # Each user can have unique meal times
#     breakfast_start_time = models.TimeField()
#     breakfast_end_time = models.TimeField()
#     lunch_start_time = models.TimeField()
#     lunch_end_time = models.TimeField()
#     tea_snack_start_time = models.TimeField()
#     from django.db import models

# class MealTime(models.Model):
#     MEAL_CHOICES = [
#         ('Breakfast', 'Breakfast'),
#         ('Lunch', 'Lunch'),
#         ('Tea & Snacks', 'Tea & Snacks'),
#         ('Dinner', 'Dinner'),
#     ]
#
#     name = models.CharField(max_length=20, choices=MEAL_CHOICES, unique=True)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def __str__(self):
#         return f"{self.name} ({self.start_time} - {self.end_time})"


from django.db import models


class MealTimeConfig(models.Model):
    name = models.CharField(max_length=20, default="Meal Time Config", unique=True)

    def __str__(self):
        return f"{self.id}"

class MealTime(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Tea & Snacks', 'Tea & Snacks'),
        ('Dinner', 'Dinner'),
    ]
    config = models.ForeignKey(MealTimeConfig, on_delete=models.CASCADE, related_name="meal_times", null=True)
    name = models.CharField(max_length=20, choices=MEAL_CHOICES, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
