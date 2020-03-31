from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    citedby = models.TextField()
    attributes = models.TextField()
    page = models.TextField()
    email = models.TextField()
    interests = models.TextField()
    url_picture = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.name
    class Meta:
        db_table = 'googlescholarauthors'
