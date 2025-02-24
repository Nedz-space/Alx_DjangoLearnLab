from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    library = models.ForeignKey('Library', related_name='books', on_delete=models.CASCADE, default=1)  # 👈 Default ID
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
