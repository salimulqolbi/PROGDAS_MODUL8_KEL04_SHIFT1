from seat import Seat

class VIPSeat(Seat):
    def __init__(self, row, col):
        super().__init__(row, col, seat_type="VIP")

    def get_price(self):
        return 70000
