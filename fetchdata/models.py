from django.db import models


class Ticket(models.Model):

    name = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)