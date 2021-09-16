from django.db import models


# Create your models here.

class ISBN(models.Model):
    ISBN_10 = models.CharField(max_length=10, blank=True)
    ISBN_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        if self.ISBN_13:
            return self.ISBN_13
        else:
            return self.ISBN_10


class Book(models.Model):
    # blank if false in validation it will require the field to not be empty
    # unique distinct entry no duplicate allowed if true
    # null If True, Django will store empty values as NULL in the database. Default is False.
    # choices specify limited choice like for rating => for select in html
    title = models.CharField(max_length=36, null=True, blank=True, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="covers/", blank=True)
    ISBN = models.OneToOneField(
        ISBN,
        null=True
        , blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book,related_name='authors')

    def __str__(self):
        return self.first_name + ' ' +self.last_name