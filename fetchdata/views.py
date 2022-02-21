from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from fetchdata.models import Ticket
from fetchdata.serializers import TicketSerializer


class TicketListView(APIView):

    def get_object(self):
        try:
            return Ticket.objects.all()
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        queryset = self.get_object()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)