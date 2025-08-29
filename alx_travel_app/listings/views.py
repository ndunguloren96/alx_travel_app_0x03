from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email_task

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed, created, updated or deleted.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        """
        Set the owner of the listing to the current user on creation.
        """
        serializer.save(owner=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed, created, updated or deleted.
    """
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        """
        Set the guest of the booking to the current user on creation
        and trigger a background email notification task.
        """
        # Ensure the listing exists before creating a booking
        listing_id = self.request.data.get('listing')
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            raise serializers.ValidationError({"listing": "Listing not found."})

        # Save the booking instance
        booking = serializer.save(guest=self.request.user, listing=listing)

        # Trigger the Celery task to send a booking confirmation email
        send_booking_confirmation_email_task.delay(booking.id)

    def get_queryset(self):
        """
        Optionally restricts the returned bookings to a given user,
        by filtering against a `guest` query parameter in the URL.
        Or against the current authenticated user.
        """
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            # Show all bookings if admin, otherwise only show user's bookings
            if user.is_staff: # or whatever condition you use for admin users
                return queryset
            return queryset.filter(guest=user)
        return Booking.objects.none() # Don't show bookings to unauthenticated users
