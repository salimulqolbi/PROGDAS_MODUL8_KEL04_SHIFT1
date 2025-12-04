class Ticket:
    def __init__(self, film, seat, schedule):
        self.film = film
        self.seat = seat
        self.schedule = schedule
        self.total_price = film.base_price + seat.get_price()
