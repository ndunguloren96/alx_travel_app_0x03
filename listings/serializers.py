from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User

class ListingSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'max_guests', 'number_of_beds', 'number_of_baths',
            'amenities', 'image_url', 'created_at', 'updated_at', 'owner', 'owner_username'
        ]
        read_only_fields = ['owner'] # Owner should be set automatically on creation

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    guest_username = serializers.CharField(source='guest.username', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'guest_username',
            'check_in_date', 'check_out_date', 'total_price', 'created_at'
        ]
        read_only_fields = ['guest'] # Guest should be set automatically on creation
