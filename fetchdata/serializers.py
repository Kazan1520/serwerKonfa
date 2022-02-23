from rest_framework import serializers
from fetchdata.models import *


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('name', 'approved')
