from django.db import models

from urlshortener.utils import create_shortned_url


class Shortner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return f"{self.long_url} to {self.short_url}"

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortned_url(self)

        super().save(*args, **kwargs)
