from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import CASCADE

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """ Ads model """
    image = models.ImageField(upload_to="images/", verbose_name="ad image", **NULLABLE)
    title = models.CharField(max_length=255, verbose_name="ad name")
    price = models.IntegerField(verbose_name="ad price")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='ad author',
                               **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="ad creation date and time")
    description = models.TextField(verbose_name="ad description")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "ad"
        verbose_name_plural = "ad"
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name="comment text")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='comment author',
                               **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=CASCADE, verbose_name='the ad under which the review was left', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="comment creation date and time")

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
