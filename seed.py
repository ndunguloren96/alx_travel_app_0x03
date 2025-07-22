import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review

class Command(BaseCommand):
    help = 'Seeds the database with sample data for listings, bookings, and reviews.'

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # Clear existing data (optional, but good for fresh seeds)
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        User.objects.filter(is_superuser=False).delete() # Keep superuser, delete others

        # Create sample users if they don't exist
        try:
            user1 = User.objects.get(username='host1')
        except User.DoesNotExist:
            user1 = User.objects.create_user(username='host1', email='host1@example.com', password='password123')
            self.stdout.write(self.style.SUCCESS('Created user: host1'))

        try:
            user2 = User.objects.get(username='host2')
        except User.DoesNotExist:
            user2 = User.objects.create_user(username='host2', email='host2@example.com', password='password123')
            self.stdout.write(self.style.SUCCESS('Created user: host2'))

        try:
            guest1 = User.objects.get(username='guest1')
        except User.DoesNotExist:
            guest1 = User.objects.create_user(username='guest1', email='guest1@example.com', password='password123')
            self.stdout.write(self.style.SUCCESS('Created user: guest1'))

        try:
            guest2 = User.objects.get(username='guest2')
        except User.DoesNotExist:
            guest2 = User.objects.create_user(username='guest2', email='guest2@example.com', password='password123')
            self.stdout.write(self.style.SUCCESS('Created user: guest2'))


        # Create sample listings
        listings_data = [
            {
                'title': 'Cozy Apartment in Nairobi CBD',
                'description': 'A charming and cozy apartment right in the heart of Nairobi. Perfect for tourists and business travelers.',
                'address': 'Koinange Street, CBD',
                'city': 'Nairobi',
                'country': 'Kenya',
                'price_per_night': 5000.00,
                'max_guests': 4,
                'number_of_beds': 2,
                'number_of_baths': 1.5,
                'amenities': 'Wifi, Kitchen, TV, Air Conditioning',
                'image_url': 'https://example.com/images/nairobi_apt.jpg',
                'owner': user1
            },
            {
                'title': 'Beachfront Villa in Diani',
                'description': 'Stunning villa with direct beach access in beautiful Diani. Enjoy the ocean breeze and relaxation.',
                'address': 'Ukunda, Diani Beach Road',
                'city': 'Diani',
                'country': 'Kenya',
                'price_per_night': 15000.00,
                'max_guests': 8,
                'number_of_beds': 4,
                'number_of_baths': 3.0,
                'amenities': 'Private Pool, Wifi, Kitchen, Ocean View, BBQ',
                'image_url': 'https://example.com/images/diani_villa.jpg',
                'owner': user2
            },
            {
                'title': 'Safari Tent in Maasai Mara',
                'description': 'Experience the wild in comfort. Luxury safari tent within a conservancy near Maasai Mara.',
                'address': 'Maasai Mara National Reserve',
                'city': 'Narok',
                'country': 'Kenya',
                'price_per_night': 25000.00,
                'max_guests': 2,
                'number_of_beds': 1,
                'number_of_baths': 1.0,
                'amenities': 'Game Drives, All-inclusive Meals, Hot Shower, Solar Power',
                'image_url': 'https://example.com/images/mara_tent.jpg',
                'owner': user1
            },
             {
                'title': 'Charming Cottage in Naivasha',
                'description': 'A serene cottage perfect for a weekend getaway near Lake Naivasha. Enjoy nature and tranquility.',
                'address': 'Moi South Lake Road',
                'city': 'Naivasha',
                'country': 'Kenya',
                'price_per_night': 7500.00,
                'max_guests': 6,
                'number_of_beds': 3,
                'number_of_baths': 2.0,
                'amenities': 'Garden, BBQ, Fireplace, Lake Access',
                'image_url': 'https://example.com/images/naivasha_cottage.jpg',
                'owner': user2
            }
        ]

        created_listings = []
        for data in listings_data:
            listing = Listing.objects.create(**data)
            created_listings.append(listing)
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        # Create sample bookings
        if created_listings:
            today = date.today()

            # Booking for the first listing by guest1
            Booking.objects.create(
                listing=created_listings[0],
                guest=guest1,
                check_in_date=today + timedelta(days=7),
                check_out_date=today + timedelta(days=10),
                total_price=created_listings[0].price_per_night * 3
            )
            self.stdout.write(self.style.SUCCESS(f'Created booking for {created_listings[0].title}'))

            # Booking for the second listing by guest2
            Booking.objects.create(
                listing=created_listings[1],
                guest=guest2,
                check_in_date=today + timedelta(days=15),
                check_out_date=today + timedelta(days=17),
                total_price=created_listings[1].price_per_night * 2
            )
            self.stdout.write(self.style.SUCCESS(f'Created booking for {created_listings[1].title}'))

            # Booking for the third listing by guest1
            Booking.objects.create(
                listing=created_listings[2],
                guest=guest1,
                check_in_date=today + timedelta(days=20),
                check_out_date=today + timedelta(days=21),
                total_price=created_listings[2].price_per_night * 1
            )
            self.stdout.write(self.style.SUCCESS(f'Created booking for {created_listings[2].title}'))

            # Create sample reviews
            # Review for the first listing by guest1
            Review.objects.create(
                listing=created_listings[0],
                guest=guest1,
                rating=5,
                comment='Absolutely loved this place! Very clean and centrally located.',
            )
            self.stdout.write(self.style.SUCCESS(f'Created review for {created_listings[0].title}'))

            # Review for the second listing by guest2
            Review.objects.create(
                listing=created_listings[1],
                guest=guest2,
                rating=4,
                comment='Great view, but a bit far from local shops.',
            )
            self.stdout.write(self.style.SUCCESS(f'Created review for {created_listings[1].title}'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
