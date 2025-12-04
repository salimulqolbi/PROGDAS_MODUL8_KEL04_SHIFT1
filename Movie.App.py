# KELOMPOK 4 SHIFT 1
# Hesya Albi Prasya     (21120125120013)
# Raudatul Khairanis    (21120125120014)
# Ibrahim Abyan Movic   (21120125120015)
# Muhamad Salimul Qolbi (21120125120016)

import customtkinter as ctk
from film import Film
from cinema import Cinema
from ticket import Ticket
import os
from PIL import Image
import random
import string

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BACKGROUND = "#020617"
CARD_BG = "#0f172a"
ACCENT = "#fbbf24"
TEXT_PRIMARY = "white"
TEXT_SECONDARY = "#9ca3af"

class MovieCard(ctk.CTkFrame):
    def __init__(self, master, movie_obj, on_click, *args, **kwargs):
        super().__init__(master, corner_radius=20, fg_color=CARD_BG, *args, **kwargs)

        self.movie = movie_obj
        self.on_click = on_click

        self.poster = ctk.CTkFrame(self, height=230, corner_radius=20, fg_color="#1e293b")
        self.poster.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 0))

        poster_path = self.get_poster_path(movie_obj.title)

        if poster_path:
            img = Image.open(poster_path)
            self.poster_img = ctk.CTkImage(light_image=img, size=(180, 230))
            ctk.CTkLabel(self.poster, image=self.poster_img, text="", fg_color="transparent").pack(expand=True)
        else:
            ctk.CTkLabel(
                self.poster, text="No Image", text_color="white"
            ).pack(expand=True)

        self.rating_badge = ctk.CTkLabel(
            self.poster, text=f"★ {movie_obj.rating}", fg_color=ACCENT,
            text_color="black", corner_radius=999, padx=10, pady=2,
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.rating_badge.place(relx=0.97, rely=0.05, anchor="ne")

        self.title_label = ctk.CTkLabel(
            self, text=movie_obj.title, text_color=TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"), anchor="w"
        )
        self.title_label.grid(row=1, column=0, sticky="ew", padx=12, pady=(10, 4))

        self.subtitle_label = ctk.CTkLabel(
            self, text=f"{movie_obj.duration} • {movie_obj.genre}",
            text_color=TEXT_SECONDARY, anchor="w", font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))

        self.bind("<Button-1>", lambda e: self.on_click(self.movie))
        for child in self.winfo_children():
            child.bind("<Button-1>", lambda e: self.on_click(self.movie))

    def get_poster_path(self, film_title):
        folder = "resources"

        title_clean = (
            film_title.lower()
            .replace(" ", "")
            .replace("-", "")
            .replace("_", "")
            .replace(":", "")
        )

        special_map = {
            "kimetsunoyaibatheinfinitycastle": "kny.jpg",
            "agaklaen2": "agak_laen_2.jpeg",
            "avatar2": "avatar.jpeg",
            "theoppenheimer": "Oppenheimer.jpg",
        }

        if title_clean in special_map:
            return os.path.join(folder, special_map[title_clean])

        for file in os.listdir(folder):
            file_clean = (
                file.lower()
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .replace(":", "")
            )
            if title_clean in file_clean and file.lower().endswith((".jpg", ".jpeg", ".png")):
                return os.path.join(folder, file)

        return None

    def __init__(self, master, movie_obj, on_click, *args, **kwargs):
        super().__init__(master, corner_radius=20, fg_color=CARD_BG, *args, **kwargs)

        self.movie = movie_obj
        self.on_click = on_click

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        poster_container = ctk.CTkFrame(self, height=230, corner_radius=20, fg_color="#1e293b")
        poster_container.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 0))

        try:
            img = self.load_poster(movie_obj.title)
            self.poster_img = ctk.CTkImage(light_image=img, size=(160, 220))
            ctk.CTkLabel(poster_container, image=self.poster_img, text="").pack(expand=True)
        except:
            ctk.CTkLabel(
                poster_container, text="No Poster", text_color="#9ca3af"
            ).pack(expand=True)

        self.rating_badge = ctk.CTkLabel(
            poster_container, text=f"★ {movie_obj.rating}", fg_color=ACCENT,
            text_color="black", corner_radius=999, padx=10, pady=2,
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.rating_badge.place(relx=0.97, rely=0.05, anchor="ne")

        # Title
        self.title_label = ctk.CTkLabel(
            self, text=movie_obj.title, text_color=TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"), anchor="w"
        )
        self.title_label.grid(row=1, column=0, sticky="ew", padx=12, pady=(10, 4))

        # Subtitle (genre + duration)
        self.subtitle_label = ctk.CTkLabel(
            self, text=f"{movie_obj.genre} • {movie_obj.duration}",
            text_color=TEXT_SECONDARY, anchor="w", font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))

        # make card clickable
        self.bind("<Button-1>", lambda e: self.on_click(self.movie))
        for child in self.winfo_children():
            child.bind("<Button-1>", lambda e: self.on_click(self.movie))

    def load_poster(self, film_title):
        folder = "resources"

        t = film_title.lower().replace(" ", "").replace(":", "").replace("-", "")

        special_map = {
            "agaklaen2": "agak_laen_2.jpeg",
            "avatar2": "avatar.jpeg",
            "kimetsunoyaibatheinfinitycastle": "kny.jpg",
            "theoppenheimer": "Oppenheimer.jpg"
        }

        if t in special_map:
            path = os.path.join(folder, special_map[t])
            return Image.open(path)

        for file in os.listdir(folder):
            clean = file.lower().replace(" ", "").replace("_", "").replace("-", "")
            if t in clean:
                return Image.open(os.path.join(folder, file))

        raise FileNotFoundError("Poster not found")

    def __init__(self, master, movie_obj, on_click, *args, **kwargs):
        super().__init__(master, corner_radius=20, fg_color=CARD_BG, *args, **kwargs)

        self.movie = movie_obj
        self.on_click = on_click

        # GRID
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # POSTER
        self.poster_frame = ctk.CTkFrame(
            self, height=230, corner_radius=20, fg_color="#1e293b"
        )
        self.poster_frame.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 0))

        self.poster_img = self.load_poster(movie_obj.title)
        if self.poster_img:
            poster_label = ctk.CTkLabel(
                self.poster_frame,
                image=self.poster_img,
                text="",
                fg_color="transparent"
            )
            poster_label.pack(expand=True, fill="both")
        else:
            ctk.CTkLabel(
                self.poster_frame,
                text="No Poster",
                text_color="#9ca3af"
            ).pack(expand=True)

        # RATING BADGE
        self.rating_badge = ctk.CTkLabel(
            self.poster_frame,
            text=f"★ {movie_obj.rating}",
            fg_color=ACCENT,
            text_color="black",
            corner_radius=999,
            padx=10,
            pady=2,
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.rating_badge.place(relx=0.97, rely=0.05, anchor="ne")

        # TITLE
        self.title_label = ctk.CTkLabel(
            self, text=movie_obj.title, text_color=TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.title_label.grid(row=1, column=0, sticky="ew", padx=12, pady=(10, 2))

        # GENRE + DURATION
        self.subtitle_label = ctk.CTkLabel(
            self, text=f"{movie_obj.genre} • {movie_obj.duration}",
            text_color=TEXT_SECONDARY,
            font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 10))

        # MAKE ENTIRE CARD CLICKABLE
        self.bind("<Button-1>", lambda e: self.on_click(self.movie))
        for child in self.winfo_children():
            child.bind("<Button-1>", lambda e: self.on_click(self.movie))

    # POSTER LOADING FUNCTION
    def load_poster(self, film_title):
        folder = "resources"

        title_clean = (
            film_title.lower()
            .replace(" ", "")
            .replace("-", "")
            .replace("_", "")
            .replace(":", "")
        )

        # MANUAL MAP FOR MISS-MATCH TITLES
        map_special = {
            "agaklaen2": "agak_laen_2.jpeg",
            "kimetsunoyaibatheinfinitycastle": "kny.jpg",
            "avatar2": "avatar.jpeg",
            "theoppenheimer": "Oppenheimer.jpg"
        }

        # PRIORITY #1 – INDIRECT MATCH
        if title_clean in map_special:
            filename = map_special[title_clean]
            path = os.path.join(folder, filename)
            if os.path.exists(path):
                return self.scale_image(path)

        # PRIORITY #2 – AUTO FIND BY NAME
        for file in os.listdir(folder):
            file_clean = (
                file.lower()
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .replace(":", "")
            )
            if title_clean in file_clean:
                return self.scale_image(os.path.join(folder, file))

        return None

    # AUTO SCALE POSTER
    def scale_image(self, path):
        img = Image.open(path)
        orig_w, orig_h = img.size

        max_w, max_h = 200, 230  # cocok untuk card kecil home page

        ratio = min(max_w / orig_w, max_h / orig_h)
        new_w = int(orig_w * ratio)
        new_h = int(orig_h * ratio)

        return ctk.CTkImage(light_image=img, size=(new_w, new_h))
    def __init__(self, master, movie_obj, on_click, *args, **kwargs):
        super().__init__(master, corner_radius=20, fg_color=CARD_BG, *args, **kwargs)

        self.movie = movie_obj
        self.on_click = on_click

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.poster = ctk.CTkFrame(self, height=230, corner_radius=20, fg_color="#1e293b")
        self.poster.grid(row=0, column=0, sticky="nsew", padx=8, pady=(8, 0))

        self.rating_badge = ctk.CTkLabel(
            self.poster, text=f"★ {movie_obj.rating}", fg_color=ACCENT,
            text_color="black", corner_radius=999, padx=10, pady=2,
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.rating_badge.place(relx=0.97, rely=0.05, anchor="ne")

        self.title_label = ctk.CTkLabel(
            self, text=movie_obj.title, text_color=TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"), anchor="w"
        )
        self.title_label.grid(row=1, column=0, sticky="ew", padx=12, pady=(10, 4))

        self.subtitle_label = ctk.CTkLabel(
            self, text=f"{movie_obj.genre} • {movie_obj.duration}",
            text_color=TEXT_SECONDARY, anchor="w", font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))

        self.bind("<Button-1>", lambda e: self.on_click(self.movie))
        for child in self.winfo_children():
            child.bind("<Button-1>", lambda e: self.on_click(self.movie))

class MovieApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Movie Ticket Booking - Now Showing")
        self.geometry("1280x720")
        self.configure(fg_color=BACKGROUND)

        self.active_category = "All"
        self.selected_seat = None

        self.cinema = Cinema()
        self.load_films()
        self.cinema.create_seats()

        self.build_main_page()

        
    def generate_booking_id(self):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(10))

    def load_films(self):
        self.cinema.add_film(Film("Agak Laen 2", "Comedy", "2h 10m", 8.7, 30000))
        self.cinema.add_film(Film("Avatar 2", "Drama, Action, Sci-Fi", "1h 55m", 7.5, 28000))
        self.cinema.add_film(Film("Kimetsu No Yaiba : The Infinity Castle", "Action", "2h 30m", 8.2, 35000))
        self.cinema.add_film(Film("The Oppenheimer", "Drama, Thriller", "1h 40m", 7.9, 27000))

    def build_main_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        if hasattr(self, "confirm_btn"):
            del self.confirm_btn
        self.selected_seat = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=40, pady=(30, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(
            header, text="History", width=120, height=40,
            fg_color="#1e40af", hover_color="#1e3a8a",
            command=self.build_history_page
        ).grid(row=0, column=1, sticky="e")

        ctk.CTkLabel(
            header, text="Now Showing", text_color=TEXT_PRIMARY,
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            header, text="Book your favorite movies",
            text_color=TEXT_SECONDARY, font=ctk.CTkFont(size=14)
        ).grid(row=1, column=0, sticky="w")

        search = ctk.CTkFrame(self, fg_color="transparent")
        search.grid(row=1, column=0, sticky="ew", padx=40, pady=(10, 10))
        search.grid_columnconfigure(0, weight=1)

        ctk.CTkEntry(
            search, placeholder_text="Search movies...",
            height=45, corner_radius=999, fg_color="#020617",
            border_width=0, text_color=TEXT_PRIMARY
        ).grid(row=0, column=0, sticky="ew")

        filter_frame = ctk.CTkFrame(self, fg_color="transparent")
        filter_frame.grid(row=2, column=0, sticky="w", padx=40, pady=(5, 10))

        categories = ["All"]
        for i, cat in enumerate(categories):
            is_active = (cat == self.active_category)
            btn = ctk.CTkButton(
                filter_frame, text=cat, corner_radius=999, width=80, height=32,
                fg_color=ACCENT if is_active else "#020617",
                hover_color="#facc15" if is_active else "#111827",
                text_color="black" if is_active else TEXT_PRIMARY,
                command=lambda c=cat: self.apply_filter(c)
            )
            btn.grid(row=0, column=i, padx=8)

        grid = ctk.CTkScrollableFrame(self, fg_color="transparent")
        grid.grid(row=3, column=0, sticky="nsew", padx=15, pady=(5, 20))
        for i in range(6):
            grid.grid_columnconfigure(i, weight=0)

        if self.active_category == "All":
            movies = self.cinema.films
        else:
            movies = []
            target = self.active_category.lower()
            for m in self.cinema.films:
                genres = [g.strip().lower() for g in m.genre.split(",") if g.strip()]
                if target in genres:
                    movies.append(m)

        for index, movie in enumerate(movies):
            row = index // 4
            col = index % 4
            card = MovieCard(grid, movie, self.open_schedule_page, width=180, height=280)
            card.grid(row=row, column=col, padx=5, pady=5)

    def open_schedule_page(self, film):
        self.selected_film = film
        self.selected_schedule = None

        # clear window
        for widget in self.winfo_children():
            widget.destroy()

        # === BACK BUTTON ===
        back_btn = ctk.CTkButton(
            self,
            text="◀  Back to Movies",
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="white",
            anchor="w",
            width=150,
            command=self.build_main_page,
        )
        back_btn.pack(padx=20, pady=(20, 10), anchor="w")

        # === MAIN SCROLL ===
        main_scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        main_scroll.pack(fill="both", expand=True, padx=20, pady=10)

        # === MOVIE FRAME ===
        movie_frame = ctk.CTkFrame(main_scroll, fg_color="#111a2e", corner_radius=20)
        movie_frame.pack(padx=20, pady=10, fill="x")
        movie_frame.grid_columnconfigure(1, weight=1)

        # === POSTER AREA ===
        poster_frame = ctk.CTkFrame(
            movie_frame, width=350, height=500,
            fg_color="#1e293b", corner_radius=20
        )
        poster_frame.grid(row=0, column=0, padx=20, pady=20)

        # === LOAD POSTER FILE ===
        def get_poster_path(title):
            folder = "resources"

            title_clean = (
                title.lower()
                .replace(" ", "")
                .replace("-", "")
                .replace(":", "")
                .replace("_", "")
            )

            special_override = {
                "agaklaen2": "agak_laen_2.jpeg",
                "avatar2": "avatar.jpeg",
                "kimetsunoyaibatheinfinitycastle": "kny.jpg",
                "theoppenheimer": "Oppenheimer.jpg"
            }

            if title_clean in special_override:
                return os.path.join(folder, special_override[title_clean])

            for file in os.listdir(folder):
                check = file.lower().replace(" ", "").replace("_", "").replace("-", "")
                if title_clean in check and file.lower().endswith((".jpg", ".jpeg", ".png")):
                    return os.path.join(folder, file)

            return None

        poster_path = get_poster_path(film.title)

        if poster_path:
            img = Image.open(poster_path)
            orig_w, orig_h = img.size

            max_w, max_h = 350, 500
            ratio = min(max_w/orig_w, max_h/orig_h)

            new_w = int(orig_w * ratio)
            new_h = int(orig_h * ratio)

            self.schedule_poster_img = ctk.CTkImage(img, size=(new_w, new_h))

            ctk.CTkLabel(
                poster_frame,
                image=self.schedule_poster_img,
                text=""
            ).pack(expand=True, padx=10, pady=10)
        else:
            ctk.CTkLabel(
                poster_frame,
                text="Poster Not Found",
                text_color="#9ca3af",
                font=ctk.CTkFont(size=20, weight="bold")
            ).pack(expand=True)

        # === INFO PANEL ===
        info_frame = ctk.CTkFrame(movie_frame, fg_color="transparent")
        info_frame.grid(row=0, column=1, sticky="nw", padx=20, pady=20)

        ctk.CTkLabel(
            info_frame, text=film.title,
            text_color="white",
            font=ctk.CTkFont(size=32, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            info_frame,
            text=f"⭐ {film.rating}/10     🎬 {film.genre}     ⏱ {film.duration}",
            text_color="#d1d5db",
            font=ctk.CTkFont(size=15)
        ).pack(anchor="w", pady=(10, 20))

        # === SHOWTIME SELECTION ===
        showtime_frame = ctk.CTkFrame(main_scroll, fg_color="#111a2e", corner_radius=20)
        showtime_frame.pack(padx=20, pady=20, fill="x")

        ctk.CTkLabel(
            showtime_frame,
            text="Select Showtime",
            text_color="white",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(pady=20)

        btn_container = ctk.CTkFrame(showtime_frame, fg_color="transparent")
        btn_container.pack(fill="x", padx=20, pady=10)

        columns = 5
        for col in range(columns):
            btn_container.grid_columnconfigure(col, weight=1)

        times = ["10:00", "13:00", "16:00", "19:00", "22:00"]

        # continue button
        self.continue_btn = ctk.CTkButton(
            showtime_frame,
            text="Continue to Seat Selection",
            corner_radius=15,
            height=55,
            fg_color="#334155",
            hover_color="#1f2937",
            text_color="#9ca3af",
            state="disabled",
            command=self.build_seat_page,
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.continue_btn.pack(fill="x", padx=20, pady=(15, 25))

        # handle showtime click
        def pick_time(selected, button):
            self.selected_schedule = selected
            for child in btn_container.winfo_children():
                child.configure(fg_color=CARD_BG, text_color="white")
            button.configure(fg_color=ACCENT, text_color="black")

            self.continue_btn.configure(
                fg_color=ACCENT,
                hover_color="#facc15",
                text_color="black",
                state="normal"
            )

        for i, sc in enumerate(times):
            btn = ctk.CTkButton(
                btn_container,
                text=f"{sc}\nAvailable",
                height=90,
                corner_radius=15,
                fg_color=CARD_BG,
                hover_color="#334155",
                text_color="white",
                font=ctk.CTkFont(size=18, weight="bold")
            )
            btn.grid(row=0, column=i, padx=6, pady=5, sticky="nsew")
            btn.configure(command=lambda s=sc, b=btn: pick_time(s, b))


    def pick_schedule(self, schedule):
        self.selected_schedule = schedule
        self.build_seat_page()

    def build_seat_page(self):

        for widget in self.winfo_children():
            widget.destroy()

        page = ctk.CTkScrollableFrame(self, fg_color="transparent")
        page.pack(fill="both", expand=True)

        back_btn = ctk.CTkButton(
            page, text="◀ Back to Schedule",
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="white",
            anchor="w",
            command=lambda: self.open_schedule_page(self.selected_film)
        )
        back_btn.pack(padx=20, pady=(10, 5), anchor="w")

        header = ctk.CTkFrame(page, fg_color="#111a2e", corner_radius=20)
        header.pack(fill="x", padx=20, pady=10)

        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header, text=self.selected_film.title,
            text_color="white", font=ctk.CTkFont(size=28, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

        ctk.CTkLabel(
            header,
            text=f"{self.selected_schedule} • {self.selected_film.duration}",
            text_color="#d1d5db", font=ctk.CTkFont(size=15)
        ).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))

        price_frame = ctk.CTkFrame(header, fg_color="transparent")
        price_frame.grid(row=0, column=1, rowspan=2, padx=20)

        self.total_price_var = ctk.StringVar(value="Rp 0")

        ctk.CTkLabel(
            price_frame, text="Total Price",
            text_color="#9ca3af", font=ctk.CTkFont(size=15)
        ).pack(anchor="e")

        self.total_price_label = ctk.CTkLabel(
            price_frame, textvariable=self.total_price_var,
            text_color=ACCENT, font=ctk.CTkFont(size=22, weight="bold")
        )
        self.total_price_label.pack(anchor="e")

        screen_bar = ctk.CTkFrame(page, fg_color="#1e293b", corner_radius=10, height=5)
        screen_bar.pack(fill="x", padx=200, pady=(10, 5))

        ctk.CTkLabel(
            page, text="SCREEN", text_color="#9ca3af",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(0, 20))

        seat_area = ctk.CTkFrame(page, fg_color="transparent")
        seat_area.pack(pady=10)

        self.selected_seats = []

        for r, row in enumerate(self.cinema.seats):
            row_frame = ctk.CTkFrame(seat_area, fg_color="transparent")
            row_frame.pack()

            row_label = ctk.CTkLabel(
                row_frame, text=chr(65 + r), text_color="white",
                width=20, font=ctk.CTkFont(size=15)
            )
            row_label.pack(side="left")

            for c, seat in enumerate(row):

                default_color = (
                    "#991b1b" if seat.booked else
                    ("#fbbf24" if seat.seat_type == "VIP" else "#3b82f6")
                )

                btn = ctk.CTkButton(
                    row_frame,
                    text="",
                    width=40, height=40,
                    fg_color=default_color,
                    hover_color="#0ea5e9",
                    corner_radius=8,
                    command=lambda s=seat, b=seat: self.toggle_seat(s)
                )
                btn.pack(side="left", padx=5, pady=5)

                seat.button = btn 

        legend = ctk.CTkFrame(page, fg_color="transparent")
        legend.pack(pady=20)

        def make_legend(color, label):
            row = ctk.CTkFrame(legend, fg_color="transparent")
            row.pack(side="left", padx=15)
            ctk.CTkFrame(row, width=20, height=20, fg_color=color, corner_radius=5).pack(side="left")
            ctk.CTkLabel(row, text=f"  {label}", text_color="white").pack(side="left")

        make_legend("#3b82f6", "Regular")
        make_legend("#fbbf24", "VIP")
        make_legend("#22c55e", "Selected")
        make_legend("#991b1b", "Booked")

        self.book_btn = ctk.CTkButton(
            page, text="Book 0 Tickets – Rp 0",
            fg_color="#334155", hover_color="#1e3a8a", 
            height=60, corner_radius=20,
            state="disabled",
            command=self.build_summary_page,
            text_color="#000000",
        )
        self.book_btn.pack(fill="x", padx=20, pady=20)

    def toggle_seat(self, seat):
            if seat.booked:
                return

            if seat in self.selected_seats:
                self.selected_seats.remove(seat)
                seat.button.configure(
                    fg_color=("#fbbf24" if seat.seat_type == "VIP" else "#3b82f6")
                )
            else:
                self.selected_seats.append(seat)
                seat.button.configure(fg_color="#22c55e")

            total = sum(s.get_price() for s in self.selected_seats)

            self.total_price_var.set(f"Rp {total:,}")
            self.book_btn.configure(
                text=f"Book {len(self.selected_seats)} Tickets – Rp {total:,}",
                state="normal" if self.selected_seats else "disabled",
                fg_color=ACCENT if self.selected_seats else "#334155"
            )

    def select_seat(self, seat):
        if seat.booked:
            print("This seat is already booked!")
            return

        self.selected_seat = seat
        print(f"Selected seat: Row {seat.row+1}, Col {seat.col+1}")
        self.show_confirm_button()

    def show_confirm_button(self):
        if hasattr(self, "confirm_btn"):
            return

        self.confirm_btn = ctk.CTkButton(
            self, text="Confirm Seat",
            width=200, height=50,
            fg_color="#22c55e", hover_color="#15803d",
            command=self.confirm_booking
        )
        self.confirm_btn.pack(pady=20)

    def confirm_booking(self):
        if not getattr(self, "selected_seats", []):
            return

        self.tickets = []

        for seat in self.selected_seats:
            ticket = Ticket(self.selected_film, seat, self.selected_schedule)
            self.tickets.append(ticket)
            self.cinema.ticket_queue.append(ticket)
            self.cinema.history.append(ticket)
            seat.booked = True

        self.show_booking_success()

    def show_print_success_multi(self):
        for widget in self.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self,
            text="Booking Confirmed!",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color="#22c55e"
        ).pack(pady=40)

        seat_lines = []
        for t in self.tickets:
            row_letter = chr(65 + t.seat.row)
            col_number = t.seat.col + 1
            seat_lines.append(f"{row_letter}{col_number} ({t.seat.seat_type})")

        text = (
            f"Film : {self.selected_film.title}\n"
            f"Time : {self.selected_schedule}\n"
            f"Seats: {', '.join(seat_lines)}\n"
            f"Total: Rp {self.summary_total_price:,}"
        )

        ctk.CTkLabel(
            self,
            text=text,
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left"
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Back to Home",
            width=220,
            height=50,
            fg_color="#3b82f6",
            hover_color="#1d4ed8",
            command=self.build_main_page
        ).pack(pady=30)

    def build_summary_page(self):
        if not getattr(self, "selected_seats", []):
            return

        total_price = sum(s.get_price() for s in self.selected_seats)

        self.summary_total_price = total_price

        for widget in self.winfo_children():
            widget.destroy()

        page = ctk.CTkScrollableFrame(self, fg_color="transparent")
        page.pack(fill="both", expand=True)

        back_btn = ctk.CTkButton(
            page, text="◀ Back to Seats",
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="white",
            anchor="w",
            command=self.build_seat_page
        )
        back_btn.pack(padx=20, pady=(10, 5), anchor="w")

        banner = ctk.CTkFrame(page, fg_color="#16a34a", corner_radius=20)
        banner.pack(fill="x", padx=40, pady=(10, 20))

        ctk.CTkLabel(
            banner, text="✔  Booking Summary",
            text_color="white",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(anchor="w", padx=25, pady=(15, 0))

        ctk.CTkLabel(
            banner,
            text="Review your booking details before confirmation",
            text_color="#dcfce7",
            font=ctk.CTkFont(size=14)
        ).pack(anchor="w", padx=25, pady=(0, 15))

        card = ctk.CTkFrame(page, fg_color="#111a2e", corner_radius=20)
        card.pack(fill="x", padx=40, pady=(0, 20))

        card.grid_columnconfigure(1, weight=1)

        def get_poster_path(film_title):
            folder = "resources"
            
            title_clean = (
                film_title.lower()
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .replace(":", "")
            )

            special_map = {
                "kimetsunoyaibatheinfinitycastle": "kny.jpg",
                "agaklaen2": "agak_laen_2.jpeg",
                "avatar2": "avatar.jpeg",
                "theoppenheimer": "Oppenheimer.jpg",
            }

            if title_clean in special_map:
                return os.path.join(folder, special_map[title_clean])

            for file in os.listdir(folder):
                file_clean = (
                    file.lower()
                    .replace(" ", "")
                    .replace("-", "")
                    .replace("_", "")
                    .replace(":", "")
                )
                if title_clean in file_clean and file.lower().endswith((".jpg", ".jpeg", ".png")):
                    return os.path.join(folder, file)

            return None

        poster_container = ctk.CTkFrame(card, fg_color="#020617", corner_radius=20)
        poster_container.grid(row=0, column=0, rowspan=4, padx=25, pady=25)

        poster_path = get_poster_path(self.selected_film.title)

        if poster_path:
            img = Image.open(poster_path)
            orig_w, orig_h = img.size

            max_w, max_h = 330, 480 

            ratio = min(max_w / orig_w, max_h / orig_h)
            new_w = int(orig_w * ratio)
            new_h = int(orig_h * ratio)

            self.poster_img = ctk.CTkImage(light_image=img, size=(new_w, new_h))

            poster_label = ctk.CTkLabel(poster_container, image=self.poster_img, text="", fg_color="transparent")
            poster_label.pack(expand=True, fill="both", padx=10, pady=10)

        else:
            ctk.CTkLabel(
                poster_container,
                text="Poster\nNot Found",
                text_color="#6b7280",
                font=ctk.CTkFont(size=16, weight="bold"),
                justify="center"
            ).pack(expand=True, fill="both", padx=20, pady=20)

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.grid(row=0, column=1, sticky="nw", padx=20, pady=25)

        ctk.CTkLabel(
            info, text=self.selected_film.title,
            text_color="white",
            font=ctk.CTkFont(size=28, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        date_text = "December 3, 2025"
        cinema_text = "Cinema Hall 1"

        def info_row(row, label, value):
            frame = ctk.CTkFrame(info, fg_color="transparent")
            frame.grid(row=row, column=0, sticky="w", pady=4)
            ctk.CTkLabel(
                frame, text=label, text_color="#9ca3af",
                font=ctk.CTkFont(size=14)
            ).pack(anchor="w")
            ctk.CTkLabel(
                frame, text=value, text_color="white",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w")

        info_row(1, "Date", date_text)
        info_row(2, "Show Time", self.selected_schedule)
        info_row(3, "Cinema", cinema_text)
        info_row(4, "Genre", self.selected_film.duration)

        seats_section = ctk.CTkFrame(card, fg_color="transparent")
        seats_section.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 20))

        ctk.CTkLabel(
            seats_section, text="Selected Seats",
            text_color="white", font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=25, pady=(10, 5))

        chip_container = ctk.CTkFrame(seats_section, fg_color="transparent")
        chip_container.pack(anchor="w", padx=25, pady=(0, 5))

        for seat in self.selected_seats:
            row_letter = chr(65 + seat.row)
            col_number = seat.col + 1
            seat_text = f"{row_letter}{col_number}  {seat.seat_type}"

            chip = ctk.CTkFrame(
                chip_container, fg_color="#020617", corner_radius=999
            )
            chip.pack(side="left", padx=5, pady=5)

            ctk.CTkLabel(
                chip, text=seat_text,
                text_color="white", font=ctk.CTkFont(size=14)
            ).pack(padx=10, pady=4)

        ctk.CTkLabel(
            seats_section,
            text=f"Total {len(self.selected_seats)} seat selected",
            text_color="#9ca3af",
            font=ctk.CTkFont(size=13)
        ).pack(anchor="w", padx=25, pady=(0, 10))

        breakdown = ctk.CTkFrame(card, fg_color="transparent")
        breakdown.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 10))

        ctk.CTkLabel(
            breakdown, text="Price Breakdown",
            text_color="white", font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=25, pady=(10, 5))

        for seat in self.selected_seats:
            row_letter = chr(65 + seat.row)
            col_number = seat.col + 1
            label = f"Seat {row_letter}{col_number} ({seat.seat_type})"
            price = seat.get_price()

            row_frame = ctk.CTkFrame(breakdown, fg_color="transparent")
            row_frame.pack(fill="x", padx=25, pady=2)

            ctk.CTkLabel(
                row_frame, text=label,
                text_color="#e5e7eb", font=ctk.CTkFont(size=14)
            ).pack(side="left")

            ctk.CTkLabel(
                row_frame, text=f"Rp {price:,}",
                text_color="white", font=ctk.CTkFont(size=14)
            ).pack(side="right")

        total_frame = ctk.CTkFrame(card, fg_color="transparent")
        total_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(15, 20))

        inner = ctk.CTkFrame(total_frame, fg_color="transparent")
        inner.pack(fill="x", padx=25)

        ctk.CTkLabel(
            inner, text="Total Amount",
            text_color="#e5e7eb", font=ctk.CTkFont(size=16)
        ).pack(side="left")

        ctk.CTkLabel(
            inner, text=f"Rp {total_price:,}",
            text_color=ACCENT,
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(side="right")

        confirm_btn = ctk.CTkButton(
            page,
            text="Confirm Booking",
            fg_color=ACCENT,
            hover_color="#facc15",
            text_color="black",
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            corner_radius=20,
            command=self.confirm_booking
        )
        confirm_btn.pack(fill="x", padx=40, pady=(10, 20))

        ctk.CTkLabel(
            page,
            text="By confirming, you agree to our terms and conditions",
            text_color="#9ca3af",
            font=ctk.CTkFont(size=12)
        ).pack(pady=(0, 20))

    def print_ticket(self):
        if not self.cinema.ticket_queue:
            print("Queue Empty!")
            return

        ticket = self.cinema.ticket_queue.popleft()
        self.cinema.history.append(ticket)

        self.show_print_success(ticket)

    def show_booking_success(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.booking_id = self.generate_booking_id()

        page = ctk.CTkScrollableFrame(self, fg_color="transparent")
        page.pack(fill="both", expand=True, padx=20, pady=20)

        icon_frame = ctk.CTkFrame(page, fg_color="transparent")
        icon_frame.pack(pady=(20, 5))

        ctk.CTkLabel(
            icon_frame,
            text="✔",
            font=ctk.CTkFont(size=80, weight="bold"),
            text_color="#22c55e"
        ).pack()

        ctk.CTkLabel(
            page,
            text="Booking Confirmed!",
            text_color="white",
            font=ctk.CTkFont(size=38, weight="bold")
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            page,
            text="Your tickets have been successfully booked",
            text_color="#9ca3af",
            font=ctk.CTkFont(size=16)
        ).pack()

        container = ctk.CTkFrame(page, fg_color="transparent")
        container.pack(pady=20, fill="x")

        card_width = 460 

        card = ctk.CTkFrame(container, fg_color="#1e293b", corner_radius=20, width=card_width)
        card.pack(anchor="center", padx=20) 

        ctk.CTkLabel(
            card,
            text="Booking ID",
            text_color="#9ca3af",
            font=ctk.CTkFont(size=15)
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            card,
            text=self.booking_id,
            text_color=ACCENT,
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack()

        ctk.CTkFrame(card, height=2, fg_color="#334155").pack(
            fill="x", padx=30, pady=20
        )

        def row(label, value1, label2, value2):
            frame = ctk.CTkFrame(card, fg_color="transparent")
            frame.pack(fill="x", padx=40, pady=4)

            left = ctk.CTkFrame(frame, fg_color="transparent")
            left.pack(side="left")

            ctk.CTkLabel(left, text=label, text_color="#9ca3af").pack(anchor="w")
            ctk.CTkLabel(left, text=value1, text_color="white",
                        font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w")

            right = ctk.CTkFrame(frame, fg_color="transparent")
            right.pack(side="right")

            ctk.CTkLabel(right, text=label2, text_color="#9ca3af").pack(anchor="e")
            ctk.CTkLabel(right, text=value2, text_color="white",
                        font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="e")

        row("Movie", self.selected_film.title,
            "Show Time", self.selected_schedule)

        selected_seat_text = ", ".join(
            f"{chr(65+s.row)}{s.col+1}" for s in self.selected_seats
        )

        total_price = f"Rp {self.summary_total_price:,}"

        row("Seats", selected_seat_text,
            "Total Paid", total_price)
        
        btn_row = ctk.CTkFrame(container, fg_color="transparent")
        btn_row.pack(pady=20, anchor="center")

        back_btn = ctk.CTkButton(
            btn_row,
            text="🏠  Back to Home",
            width=200,
            height=50,
            corner_radius=15,
            fg_color="#475569",
            hover_color="#334155",
            command=self.build_main_page
        )
        back_btn.pack(side="left", padx=10)

    def build_history_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self, text="Ticket History",
            font=ctk.CTkFont(size=32, weight="bold"), text_color="white"
        ).pack(pady=30)

        frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        frame.pack(fill="both", expand=True, padx=40, pady=20)

        if len(self.cinema.history) == 0:
            ctk.CTkLabel(
                frame, text="No tickets printed yet.",
                font=ctk.CTkFont(size=18), text_color="#9ca3af"
            ).pack(pady=20)
            return

        for t in self.cinema.history:
            box = ctk.CTkFrame(frame, corner_radius=15, fg_color="#1e293b")
            box.pack(fill="x", pady=10, padx=10)

            text = (
                f"Film: {t.film.title}\n"
                f"Schedule: {t.schedule}\n"
                f"Seat: Row {t.seat.row+1}, Col {t.seat.col+1}\n"
                f"Total: Rp {t.total_price:,}"
            )
            ctk.CTkLabel(
                box, text=text, font=ctk.CTkFont(size=16),
                text_color="white", justify="left"
            ).pack(padx=15, pady=15)

        ctk.CTkButton(
            self, text="Back", width=200, height=40,
            fg_color="#475569", hover_color="#334155",
            command=self.build_main_page
        ).pack(pady=20)

    def apply_filter(self, category):
        self.active_category = category
        self.build_main_page()

if __name__ == "__main__":
    MovieApp().mainloop()
