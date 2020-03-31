from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    affiliation = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.name
    class Meta:
        db_table = 'Authors'
class Article(models.Model):
    name = models.TextField()
    affiliation = models.TextField()
    pub_title = models.TextField()
    pub_year = models.TextField()
    pub_url = models.TextField()
    citations = models.TextField()
    citedby = models.TextField()
    journal = models.TextField()
    pub_author = models.TextField()
    def __str__(self):
        """A string representation of the model."""
        return self.name
    class Meta:
        db_table = 'Articles'
