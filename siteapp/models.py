from django.db import models


# Create your models here.

class block_posts(models.Model):
    text_post = models.TextField(help_text="Текст статьи", verbose_name="Текст статьи")
    data_post = models.DateField(help_text="Дата создания статьи", verbose_name="Дата создания статьи")


def __str__(self):
    return self.text_post


