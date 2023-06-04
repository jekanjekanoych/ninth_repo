from django.db import models


class Number(models.Model):
    number = models.CharField(max_length=200)

    def __str__(self):
        return "%s %i" % (self.number, self.id)


class Code(models.Model):
    number = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %i" % (self.code, self.number, self.id)
