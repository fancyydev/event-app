from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='municipalities')

    def __str__(self):
        return self.name
