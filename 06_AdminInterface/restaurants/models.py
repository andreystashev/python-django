from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    count_of_employers = models.IntegerField()
    director = models.CharField(max_length=30)
    chef = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.IntegerField()
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    serves_sushi = models.BooleanField(default=False)
    serves_burgers = models.BooleanField(default=False)
    serves_donats = models.BooleanField(default=False)
    serves_coffee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.city})'


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.IntegerField()
    apartment = models.IntegerField()
    seniority = models.TextField()
    education = models.TextField(max_length=50)
    cources = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
