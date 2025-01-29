from django.db import models
from lessons.models import Lesson


class Test(models.Model):
    name = models.CharField(max_length=200, verbose_name='Test nomi')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="tests", verbose_name='Dars'
                                                                                                    '')

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name='Question')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions", verbose_name='Test')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField(verbose_name='Answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name='Savol')
    is_correct = models.BooleanField(default=False, verbose_name='Javob')

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"
