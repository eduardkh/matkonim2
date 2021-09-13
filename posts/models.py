from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
# Create your models here.
User = settings.AUTH_USER_MODEL
# Technique (choices)


class Technique(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
# Category (choices)


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
# Difficulty (1-5)


class Difficulty(models.Model):
    level = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.level)
# Prep Time


class PrepTime(models.Model):
    prep_time = models.IntegerField(blank=True, default=1, validators=[
        MinValueValidator(1), MaxValueValidator(10080)])

    def __str__(self):
        return str(self.prep_time)
# Cook Time


class CookTime(models.Model):
    cook_time = models.IntegerField(blank=True, default=1, validators=[
        MinValueValidator(1), MaxValueValidator(10080)])

    def __str__(self):
        return str(self.cook_time)
# Ingredient and quantity


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {str(self.quantity)}'


class Recipe(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(allow_unicode=True, db_index=True,
                            unique=True, default="", null=False, blank=True)
    author = models.ForeignKey(User, default=1,
                               on_delete=models.SET_DEFAULT)
    category = models.ManyToManyField(Category)
    techniques = models.ManyToManyField(Technique)
    difficulty = models.ForeignKey(
        Difficulty, default=1, on_delete=models.SET_DEFAULT, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='recipe_user_uploads/')
    prep_time = models.ForeignKey(
        PrepTime, default=1, on_delete=models.SET_DEFAULT, blank=True)
    cook_time = models.ForeignKey(
        CookTime, default=1, on_delete=models.SET_DEFAULT, blank=True)
    Instructions = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
