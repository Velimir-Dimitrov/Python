import os
from datetime import date, timedelta
from typing import List

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Song, Artist, Product, Review, Driver, DrivingLicense, Owner, Registration, \
    Car


# Create queries within functions


def show_all_authors_with_their_books() -> str:
    authors_with_books = Author.objects.order_by('id').filter(book_set__isnull=False)
    result = []
    for author in authors_with_books:
        books = ", ".join(book.title for book in author.book_set.all())
        result.append(f"{author.name} has written - {books}!")

    return "\n".join(result)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# # Test code for exercise 1
# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
# book4 = Book.objects.create(
#     title="Harry Potter and the Chamber of Secrets",
#     price=19.99,
#     author=author1
# )
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
#
# # Delete authors without books
# print(Author.objects.count())
# delete_all_authors_without_books()
# print(Author.objects.count())


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    return Artist.objects.get(name=artist_name).songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


# # Test code for exercise 2
# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
#
# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    reviews = Product.objects.get(name=product_name).reviews.all()
    reviews_ratings = [review.rating for review in reviews]
    average_rating = sum(reviews_ratings) / len(reviews)
    return average_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews() -> None:
    get_products_with_no_reviews().delete()

# # Test code for exercise 3
# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)
#
# # Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
#
# # Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))


def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.order_by("-license_number")
    return "\n".join(
        f"License with number: {l.license_number} expires on {l.issue_date + timedelta(days=365)}!" for l in licenses)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    latest_issue_date = due_date - timedelta(days=365)
    return Driver.objects.filter(license__issue_date__gt=latest_issue_date)


# # Test code for exercise 4
# # Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# # Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
#
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)
#
# Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
#
# # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
#
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")


def register_car_by_owner(owner: Owner) -> str:
    unregistered_car = Car.objects.filter(registration__isnull=True).first()

    free_registration = Registration.objects.filter(car__isnull=True).first()
    free_registration.registration_date = date.today()
    free_registration.car = unregistered_car
    free_registration.save()

    unregistered_car.owner = owner
    unregistered_car.save()

    return f"Successfully registered {unregistered_car.model} to {owner.name} with registration number {free_registration.registration_number}."


# # Test code for exercise 5
# # Create owners
# owner1 = Owner.objects.get(name='Ivelin Milchev')
# owner2 = Owner.objects.get(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.get(model='Citroen C5', year=2004)
# car2 = Car.objects.get(model='Honda Civic', year=2021)
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.get(registration_number='TX0044XA')
# registration2 = Registration.objects.get(registration_number='XYZ789')
#
# print(register_car_by_owner(owner1))
