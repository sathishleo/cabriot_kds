from django.db import models

# Create your models here.
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_items/')

class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredients/')

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
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
    quantity_type = models.CharField(max_length=20, choices=[
        ('g', 'Grams'), ('kg', 'Kilograms'), ('num', 'Numbers')
    ])
