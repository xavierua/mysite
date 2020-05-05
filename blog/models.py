from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    text = models.TextField(verbose_name='Текст блога')
    created_date = models.DateTimeField(verbose_name='Дата створеня', default=timezone.now)
    published_date = models.DateTimeField(verbose_name='', blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
