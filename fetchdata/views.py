from django.http import Http404
from django.shortcuts import render
from rest_framework import status
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

    def get(self, request, format=None):
        queryset = self.get_object()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(APIView):

    def get_object(self, pk):
        try:
            return Ticket.objects.filter(name=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        queryset = self.get_object(pk)
        serializer = TicketSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, pk=None, format=None):
        queryset = self.get_object(pk)
        serializer = TicketSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
