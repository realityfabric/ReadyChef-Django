from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	categories = models.ManyToManyField(Category, blank=True)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=50)
	ingredients = models.ManyToManyField(Ingredient)
	categories = models.ManyToManyField(Category, blank=True)

	def __str__(self):
		return self.name

class Pantry(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient, blank=True)
	recipes = models.ManyToManyField(Recipe, blank=True)

	def __str__(self):
		return self.user.username

