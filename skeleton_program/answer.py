from typing import Dict, List


class CinemaBookingSystem:
    def __init__(self):
        """
        Initialize the cinema booking system
        """
        self.screens: Dict[str, List[List[bool]]] = {}

    def add_screen(self, screen_name: str, rows: int, seats_per_row: int) -> None:
        """
        Adds a new screen with the specified rows and seats per row.
        """
        if screen_name in self.screens:
            raise ValueError(f"Screen {screen_name} already exists!")
        self.screens[screen_name] = [[False] * seats_per_row for _ in range(rows)]

    def book_seat(self, screen_name: str, row: int, seat: int) -> str:
        """
        Books a specific seat in the given screen.
        Returns a confirmation message if successful, otherwise an error message.
        """
        screen = self.screens.get(screen_name)
        if not screen:
            raise ValueError(f"Error: Screen {screen_name} does not exist in system.")
        if not (0 <= row-1 < len(screen)) or not (0 <= seat-1 < len(screen[0])):
            raise ValueError(f"Error: Invalid seat {seat} in row {row}")
        if screen[row-1][seat-1]:
            return f"Error: Seat {seat} in Row {row} is already booked."
        screen[row-1][seat-1] = True
        return f"Seat {seat} in Row {row} successfully booked."

    def cancel_booking(self, screen_name: str, row: int, seat: int) -> str:
        """
        Cancels the booking of a specific seat in the given screen.
        Returns a confirmation message if successful, otherwise an error message.
        """
        screen = self.screens.get(screen_name)
        if not screen:
            raise ValueError(f"Error: Screen {screen_name} does not exist in system.")
        if not (0 <= row-1 < len(screen)) or not (0 <= seat-1 < len(screen[0])):
            raise ValueError(f"Error: Invalid seat {seat} in row {row}")
        if not screen[row-1][seat-1]:
            raise ValueError(f"Error: Seat {seat} in Row {row} is not booked.")
        screen[row-1][seat-1] = False
        return f"Booking for Seat {seat} in Row {row} successfully cancelled."

    def view_available_seats(self, screen_name: str) -> list:
        """
        Returns a list of all available seats in the given screen.
        """
        screen = self.screens.get(screen_name)
        if not screen:
            raise ValueError(f"Error: Screen {screen_name} does not exist in system.")
        available_seats = [(row+1, seat+1) for seat in range(len(screen[0])) for row in range(len(screen)) if not screen[row][seat]]
        return available_seats


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
