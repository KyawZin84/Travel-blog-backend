from rest_framework import serializers
from .models import BookingModel

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookingModel
		fields=['id','name','person','place','price','date']