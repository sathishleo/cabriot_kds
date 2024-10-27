from django.db import models

class MenuItem(models.Model):
    Item_Name = models.CharField(max_length=100)
    Display_Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_items/')

    def __str__(self):
        return self.title

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
    quantity = models.FloatField()
    quantity_type = models.CharField(max_length=20, choices=[
        ('g', 'Grams'), ('kg', 'Kilograms'), ('num', 'Numbers')
    ])

    def __str__(self):
        return f"{self.menu_item} - {self.quantity} {self.get_quantity_type_display()}"

