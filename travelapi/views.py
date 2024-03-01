from django.shortcuts import render
from rest_framework import viewsets
from .models import BookingModel
from .serializers import BookingSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
	serializer_class = BookingSerializer
	queryset = BookingModel.objects.all()
	authentication_classes = (TokenAuthentication,)
