import random

# Sample movie data
movies = [
    {"title": "Movie 1", "showtimes": ["10:00 AM", "2:00 PM", "6:00 PM"]},
    {"title": "Movie 2", "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM"]},
    {"title": "Movie 3", "showtimes": ["12:00 PM", "4:00 PM", "8:00 PM"]},
]

# Booking data
bookings = []

def display_movies():
    print("\nAvailable Movies:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']}")

def display_showtimes(movie_index):
    movie = movies[movie_index]
    print("\nAvailable Showtimes:")
    for i, showtime in enumerate(movie['showtimes'], 1):
        print(f"{i}. {showtime}")

def book_ticket():
    display_movies()
    movie_index = int(input("Enter the movie number to book a ticket: ")) - 1

    if 0 <= movie_index < len(movies):
        display_showtimes(movie_index)
        showtime_index = int(input("Enter the showtime number: ")) - 1

        if 0 <= showtime_index < len(movies[movie_index]['showtimes']):
            movie = movies[movie_index]
            selected_showtime = movie['showtimes'][showtime_index]

            # Generate a random booking reference number (in a real system, this would be unique and stored in a database)
            booking_reference = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))

            # Record the booking
            bookings.append({"movie": movie['title'], "showtime": selected_showtime, "booking_ref": booking_reference})

            print(f"\nBooking successful! Your booking reference number is {booking_reference}")
        else:
            print("Invalid showtime selection.")
    else:
        print("Invalid movie selection.")

def view_bookings():
    if not bookings:
        print("No bookings available.")
    else:
        print("\nYour Bookings:")
        for i, booking in enumerate(bookings, 1):
            print(f"{i}. Movie: {booking['movie']}, Showtime: {booking['showtime']}, Booking Ref: {booking['booking_ref']}")

def main():
    while True:
        print("\nMovie Ticket Booking System")
        print("1. Book a Ticket")
        print("2. View Bookings")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            print("Thank you for using the Movie Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
