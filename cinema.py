from collections import deque
from seat import Seat
from vipSeat import VIPSeat

class Cinema:
    def __init__(self):
        self.films = []
        self.seats = []
        self.ticket_queue = deque() 
        self.history = []   

    def add_film(self, film):
        self.films.append(film)

    def create_seats(self, rows=8, cols=8):
        self.seats = []

        for r in range(rows):
            row_seats = []
            for c in range(cols):
                if r == 0:
                    row_seats.append(VIPSeat(r, c))
                else:
                    row_seats.append(Seat(r, c))
            self.seats.append(row_seats)

