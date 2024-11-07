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

class Workday(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return f"Workday on {self.date}"

class UserShift(models.Model):
    SHIFT_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Tea & Snacks', 'Tea & Snacks'),
        ('Dinner', 'Dinner'),
    ]

    workday = models.ForeignKey(Workday, on_delete=models.CASCADE, related_name='shifts')
    shift_name = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('workday', 'shift_name')

    def clean(self):
        # Check for overlapping times before saving
        existing_shifts = UserShift.objects.filter(workday=self.workday, shift_name=self.shift_name)

        for shift in existing_shifts:
            # Check if new shift times overlap with existing ones
            if (self.start_time < shift.end_time and self.end_time > shift.start_time):
                raise ValidationError(f"Shift time overlaps with an existing shift on {self.workday.date}.")

    def save(self, *args, **kwargs):
        # Call the clean method to validate before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.shift_name} Shift on {self.workday.date}"


