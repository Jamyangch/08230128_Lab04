from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):   
        return self.title

    class Meta:
        verbose_name_plural = "Learning Journey"
        

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    hobbies = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):  
        return self.name

    class Meta:
        verbose_name_plural = "About me"
