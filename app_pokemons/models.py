from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Type(models.Model):
    type_name = models.CharField(max_length=32)
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)

    class Meta:
        ordering = ('type_name', )

    def __str__(self):
        return self.type_name


class Stats(models.Model):
    stat_name = models.CharField(max_length=32)
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)

    class Meta:
        ordering = ('stat_name', )

    def __str__(self):
        return self.stat_name
