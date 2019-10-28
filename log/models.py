from django.db import models
from django.urls import reverse


class LogType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "log types"
        db_table = "LogType"

    def __str__(self):
        return self.name


class Log(models.Model):
    log_type = models.ForeignKey(LogType, null=False, on_delete=models.CASCADE)
    time = models.DateTimeField()
    info = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "logs"
        db_table = "Log"

    def __str__(self):
        return "{} [{}]: {}".format(self.time, self.info)

    def get_absolute_url(self):
        return reverse("log_type", args=(self.pk,))