from django.db import models


class Ticket(models.Model):

    name = models.CharField(primary_key=True, max_length=30)
    approved = models.BooleanField(default=False)