class Seat:
    def __init__(self, row, col, seat_type="REGULAR"):
        self.row = row
        self.col = col
        self.seat_type = seat_type
        self.booked = False

    def get_price(self):
        if self.seat_type == "REGULAR":
            return 30000
        return 50000
