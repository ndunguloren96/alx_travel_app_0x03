# listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking # Assuming Booking model is what you need

@shared_task
def send_booking_confirmation_email_task(booking_id):
    """
    Sends an email confirmation for a new booking.
    This task will run in the background.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
        subject = f'Booking Confirmation for {booking.listing.title}'
        message = (
            f'Hi {booking.guest.username},\n\n'
            f'Your booking for {booking.listing.title} has been confirmed.\n'
            f'Check-in: {booking.check_in_date}\n'
            f'Check-out: {booking.check_out_date}\n'
            f'Total Price: ${booking.total_price}\n\n'
            'Thank you for using alx_travel_app!'
        )
        recipient_list = [booking.guest.email]

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        print(f"Successfully sent booking confirmation for booking ID: {booking_id}")
    except Booking.DoesNotExist:
        print(f"Booking with ID {booking_id} not found. Task failed.")
