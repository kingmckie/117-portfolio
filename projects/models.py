from django.db import models
class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='projects_images/')
    repository = models.URLField()
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return f"{self.name} - ({self.year})"