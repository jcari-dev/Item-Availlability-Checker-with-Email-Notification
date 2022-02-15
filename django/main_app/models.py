from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import *



class Order(models.Model):
    
    product_name = models.CharField(max_length=300)
    url = models.URLField(max_length=800)
    email = models.EmailField()
    query_name = models.CharField(max_length=30)
    # email = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='order')
    date = models.DateField(default=date.today)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=35)
    
    def __str__(self):
        return self.product_name


class Product(models.Model):
    
    class Section(models.TextChoices):
        GROCERY = 'Grocery'
        HOUSEHOLD_ESSENTIALS = 'Household Essentials'
        WOMEN = 'Women'
        MEN = 'Men'
        YOUNG_ADULT = 'Young Adult'
        KIDS = 'Kids'
        SHOES = 'Shoes'
        BABY = 'Baby'
        HOME = 'Home'
        FURNITURE = 'Furniture'
        KITCHEN_AND_DINING = 'Kitchen & Dining'
        TOYS = 'Toys'
        ELECTRONICS = 'Electronics'
        VIDEO_GAMES = 'Video Games'
        MOVIES = 'Movies'
        MUSIC = 'Music'
        BOOKS = 'Books'
        SPORTS_AND_OUTDOORS = "Sports & Outdoors"
        BEAUTY = 'Beauty'
        PERSONAL_CARE = 'Personal Care'
        HEALTH = 'Health'
        PETS = 'Pets'
        LUGGAGE = 'Luggage'
        SCHOOL_AND_OFFICE_SUPPLIES = 'School & Office Supplies'
        PARTY_SUPPLIES = 'Party Supplies'
        OTHER = 'Other'
    
    category = models.CharField(choices=Section.choices, max_length=100)
    
    user = models.EmailField()
    def __str__(self):
        return self.category

class Review(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    value = models.IntegerField(choices=Rating.choices)
    user = models.CharField(max_length=20)
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='rreview')

    def __str__(self):
        return self.name
