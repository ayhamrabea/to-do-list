from django.db import models


# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
    time = models.TimeField( auto_now_add=True)

    

    class Meta:
        verbose_name = ("List")
        verbose_name_plural = ("Lists")

    def __str__(self):
        return self.title
