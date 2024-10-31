from django.db import models

class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='menu_items/',null=True,blank=True)

    def __str__(self):
        if self.display_name != None:
            return f"{self.item_name} - {self.display_name}"
        else:
            return self.item_name

class DisplaySection(models.Model):
    VEGETABLE = 'vegetable'
    MAIN = 'main'
    BREAD = 'bread'
    SECTION_CHOICES = [
        (VEGETABLE, 'Vegetable Section'),
        (MAIN, 'Main Section'),
        (BREAD, 'Bread Section'),
    ]
    name = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class DailyDisplayAssignment(models.Model):
    BREAKFAST_LUNCH = 'BL'
    DINNER = 'D'
    MEAL_PERIOD_CHOICES = [
        (BREAKFAST_LUNCH, 'Breakfast/Lunch'),
        (DINNER, 'Dinner'),
    ]

    date = models.DateField()
    meal_period = models.CharField(max_length=2, choices=MEAL_PERIOD_CHOICES)
    display_section = models.ForeignKey(DisplaySection, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_period_display()} - {self.display_section}"

class DailyDisplayMenuItem(models.Model):
    assignment = models.ForeignKey(DailyDisplayAssignment, on_delete=models.CASCADE, related_name="menu_items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10,null=True,blank=True)
    quantity_type = models.CharField(max_length=20, choices=[
        ('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Numbers', 'Numbers')
    ],null=True,blank=True)

    def __str__(self):
        display_name = self.menu_item.display_name if self.menu_item.display_name else self.menu_item.item_name
        if self.quantity is None or self.quantity_type is None:
            return display_name
        else:
            return f"{display_name} ({self.quantity} {self.quantity_type})"


