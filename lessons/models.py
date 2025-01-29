from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Dars nomi')
    desc = models.TextField(verbose_name='Dars tavsifi')

    def __str__(self):
        return self.name
