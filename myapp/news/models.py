from django.db import models

class Article(models.Model):
    title = models.CharField("title", max_length=50, default="")
    anons = models.CharField("anons", max_length=250, default="")
    full_text = models.TextField("Article")
    date = models.DateTimeField("Date Published")

    def __str__ (self):
        return {self.title} 

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"