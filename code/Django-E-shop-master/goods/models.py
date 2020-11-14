from django.db import models


# Create your models here.

class Product(models.Model):
    class Genres(models.TextChoices):
        DETECTIVE = 'det'
        HISTORICAL = 'his'
        SCI_FI = 'sci'
        ADVENTURES = 'adv'
        FANTASY = 'fan'
        BESTSELLERS = 'bes'
        FICTION = 'fic'
        FOR_CHILDREN = 'chl'

    prod_name = models.CharField(max_length=150, db_index=True)
    price = models.FloatField(db_index=True)
    prod_type = models.CharField(max_length=3, choices=Genres.choices, default='None')
    image = models.ImageField(upload_to='prods/', blank=True)
    slug = models.SlugField(max_length=50, db_index=True, default='null-slug')
    description = models.TextField(default="Описание еще не добавлено")

    def __str__(self):
        return '{}'.format(self.prod_name)
