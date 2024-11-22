class CinemaBookingSystem:
    def __init__(self):
        # Initialize the cinema booking system
        pass

    def add_screen(self, screen_name: str, rows: int, seats_per_row: int) -> None:
        """
        Adds a new screen with the specified rows and seats per row.
        """
        pass

    def book_seat(self, screen_name: str, row: int, seat: int) -> str:
        """
        Books a specific seat in the given screen.
        Returns a confirmation message if successful, otherwise an error message.
        """
        pass

    def cancel_booking(self, screen_name: str, row: int, seat: int) -> str:
        """
        Cancels the booking of a specific seat in the given screen.
        Returns a confirmation message if successful, otherwise an error message.
        """
        pass

    def view_available_seats(self, screen_name: str) -> list:
        """
        Returns a list of all available seats in the given screen.
        """
        pass


# Test Cases
if __name__ == "__main__":
    system = CinemaBookingSystem()
    
    # Add a screen
    system.add_screen("Screen1", 5, 10)
    
    # Book seats
    assert system.book_seat("Screen1", 1, 1) == "Seat 1 in Row 1 successfully booked."
    assert system.book_seat("Screen1", 1, 2) == "Seat 2 in Row 1 successfully booked."
    
    # Prevent double booking
    assert system.book_seat("Screen1", 1, 1) == "Error: Seat 1 in Row 1 is already booked."
    
    # Cancel booking
    assert system.cancel_booking("Screen1", 1, 1) == "Booking for Seat 1 in Row 1 successfully cancelled."
    
    # Book again after cancellation
    assert system.book_seat("Screen1", 1, 1) == "Seat 1 in Row 1 successfully booked."
    
    # View available seats
    available_seats = system.view_available_seats("Screen1")
    assert (1, 3) in available_seats  # Check specific seat is available
    assert (1, 1) not in available_seats  # Check booked seat is not available

    print("All tests passed!")
