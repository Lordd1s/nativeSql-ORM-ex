from django.db import models
from django.utils import timezone


# Create your models here.
class Proposes(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    contact = models.CharField(max_length=50, verbose_name="Способ связаться!") # Здесь может быть связи по типу ForeignKey по пользователям!
    title = models.CharField(max_length=50, verbose_name="Тема")
    description = models.TextField(max_length=255, verbose_name="Описание")
    date_created = models.DateTimeField(default=timezone.now())

    class Meta:
        app_label = "proposals"
        ordering = ["-date_created", "name", "title"]
        verbose_name = "Предложения или жалоба"
        verbose_name_plural = "Предложении или жалобы"

    def __str__(self):
        return f"Предложения или жалоба от {self.name} по тему: {self.title}"