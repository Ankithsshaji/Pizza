from django.db import models

class Pizza(models.Model):
    """Represents a pizza type."""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """Represents a topping for a pizza."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name