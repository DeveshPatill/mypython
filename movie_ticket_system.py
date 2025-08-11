"""
# movie_ticket_system.py
Movie Ticket Management System (CLI)

Features implemented:
- Movie, Theater, TicketSystem classes with JSON persistence
- User authentication with Admin and Customer roles
- Booking and cancellation with seat tracking and overbooking prevention
- Reports: most popular movies, theater occupancy rates
- Simple recommendation engine based on user's booking history
- Command-line menu for admin and customer actions
- Data saved to 'ticket_system_data.json' in the working directory
"""

import json
import getpass
from datetime import datetime
from collections import defaultdict, Counter
from typing import List

DATA_FILE = "ticket_system_data.json"


class Movie:
    def __init__(self, title: str, duration: int, rating: str):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.show_times = []  # list of datetime objects

    def __str__(self):
        times = " ".join(t.strftime("%Y-%m-%d %H:%M") for t in self.show_times)
        return f"{self.title} ({self.duration} min, {self.rating}) | Shows: {times if times else 'No shows yet'}"

    def add_show_time(self, show_time: datetime):
        if show_time not in self.show_times:
            self.show_times.append(show_time)
            self.show_times.sort()

    def remove_show_time(self, show_time: datetime):
        if show_time in self.show_times:
            self.show_times.remove(show_time)


class Theater:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.movies: List[Movie] = []
        # seats mapping: { show_time_str: seats_available }
        self.seats = {}

    def add_movie(self, movie: Movie):
        if any(m.title == movie.title for m in self.movies):
            raise ValueError("Movie already exists in theater.")
        self.movies.append(movie)

    def remove_movie(self, title: str):
        self.movies = [m for m in self.movies if m.title != title]

    def display_movies(self):
        if not self.movies:
            print("No movies in this theater.")
            return
        for movie in self.movies:
            print(movie)

    def display_show_times(self, movie_title: str):
        movie = self._find_movie(movie_title)
        if movie:
            for t in movie.show_times:
                print(t.strftime("%Y-%m-%d %H:%M"), f"({self.seats.get(self._time_str(t), self.capacity)} seats left)")
        else:
            print("Movie not found.")


    def book_ticket(self, movie_title: str, show_time: datetime, num_tickets: int) -> bool:
        movie = self._find_movie(movie_title)
        if not movie:
            raise ValueError("Movie not found.")

        time_str = self._time_str(show_time)
        if time_str not in self.seats:
            # initialize seats for that show time
            self.seats[time_str] = self.capacity

        if self.seats[time_str] >= num_tickets:
            self.seats[time_str] -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, movie_title: str, show_time: datetime, num_tickets: int) -> bool:
        # cancelling increases available seats. We don't track individual tickets in this simple system.
        movie = self._find_movie(movie_title)
        if not movie:
            raise ValueError("Movie not found.")
        time_str = self._time_str(show_time)
        if time_str in self.seats:
            self.seats[time_str] = min(self.capacity, self.seats[time_str] + num_tickets)
            return True
        else:
            return False

    def _find_movie(self, title: str):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    @staticmethod
    def _time_str(dt: datetime):
        return dt.strftime("%Y-%m-%d %H:%M")


class User:
    def __init__(self, username: str, password: str, role: str = "customer"):
        self.username = username
        self.password = password  # NOTE: in real systems, use hashed passwords!
        self.role = role  # 'admin' or 'customer'
        self.booking_history = []  # list of dicts: {theater, movie, show_time_str, tickets, timestamp}

    def record_booking(self, theater_name: str, movie_title: str, show_time: datetime, num_tickets: int):
        self.booking_history.append({
            "theater": theater_name,
            "movie": movie_title,
            "show_time": Theater._time_str(show_time),
            "tickets": num_tickets,
            "timestamp": datetime.now().isoformat()
        })


class TicketSystem:
    def __init__(self):
        self.theaters: List[Theater] = []
        self.users: List[User] = []

    # ---------- Theater related ----------
    def add_theater(self, theater: Theater):
        if any(t.name.lower() == theater.name.lower() for t in self.theaters):
            raise ValueError("Theater already exists.")
        self.theaters.append(theater)

    def remove_theater(self, name: str):
        self.theaters = [t for t in self.theaters if t.name.lower() != name.lower()]

    def display_theaters(self):
        if not self.theaters:
            print("No theaters available.")
            return
        for t in self.theaters:
            print(f"{t.name} (Capacity: {t.capacity})")


    # ---------- User/Auth related ----------
    def add_user(self, user: User):
        if any(u.username.lower() == user.username.lower() for u in self.users):
            raise ValueError("User already exists.")
        self.users.append(user)

    def authenticate(self, username: str, password: str) -> User:
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        raise ValueError("Invalid credentials.")


    # ---------- Persistence ----------
    def save_to_file(self, filename: str = DATA_FILE):
        payload = {
            "theaters": [],
            "users": []
        }
        for t in self.theaters:
            payload["theaters"].append({
                "name": t.name,
                "capacity": t.capacity,
                "movies": [{
                    "title": m.title,
                    "duration": m.duration,
                    "rating": m.rating,
                    "show_times": [st.strftime("%Y-%m-%d %H:%M") for st in m.show_times]
                } for m in t.movies],
                "seats": t.seats
            })
        for u in self.users:
            payload["users"].append({
                "username": u.username,
                "password": u.password,
                "role": u.role,
                "booking_history": u.booking_history
            })
        with open(filename, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"Data saved to {filename}")


    def load_from_file(self, filename: str = DATA_FILE):
        try:
            with open(filename, "r") as f:
                payload = json.load(f)
            self.theaters = []
            for t_data in payload.get("theaters", []):
                t = Theater(t_data["name"], t_data["capacity"])
                t.seats = t_data.get("seats", {})
                for m_data in t_data.get("movies", []):
                    m = Movie(m_data["title"], m_data["duration"], m_data["rating"])
                    m.show_times = [datetime.strptime(st, "%Y-%m-%d %H:%M") for st in m_data.get("show_times", [])]
                    t.add_movie(m)
                self.theaters.append(t)
            self.users = []
            for u_data in payload.get("users", []):
                u = User(u_data["username"], u_data["password"], u_data.get("role", "customer"))
                u.booking_history = u_data.get("booking_history", [])
                self.users.append(u)
            print(f"Loaded data from {filename}")
        except FileNotFoundError:
            print(f"No data file found at {filename}. Starting with empty system.")


    # ---------- Helpers ----------
    def find_theater(self, name: str):
        for t in self.theaters:
            if t.name.lower() == name.lower():
                return t
        return None

    def find_user(self, username: str):
        for u in self.users:
            if u.username == username:
                return u
        return None


    # ---------- Booking & Reports ----------
    def book(self, username: str, theater_name: str, movie_title: str, show_time: datetime, num_tickets: int):
        theater = self.find_theater(theater_name)
        if not theater:
            raise ValueError("Theater not found.")
        success = theater.book_ticket(movie_title, show_time, num_tickets)
        if success:
            user = self.find_user(username)
            if user:
                user.record_booking(theater_name, movie_title, show_time, num_tickets)
            return True
        else:
            return False

    def cancel(self, username: str, theater_name: str, movie_title: str, show_time: datetime, num_tickets: int):
        theater = self.find_theater(theater_name)
        if not theater:
            raise ValueError("Theater not found.")
        ok = theater.cancel_booking(movie_title, show_time, num_tickets)
        if ok:
            # record cancellation in user history (optional)
            user = self.find_user(username)
            if user:
                user.booking_history.append({
                    "action": "cancellation",
                    "theater": theater_name,
                    "movie": movie_title,
                    "show_time": Theater._time_str(show_time),
                    "tickets": num_tickets,
                    "timestamp": datetime.now().isoformat()
                })
            return True
        return False

    def report_most_popular_movies(self, top_n: int = 5):
        counter = Counter()
        for u in self.users:
            for b in u.booking_history:
                # include bookings only (skip cancellations)
                if b.get("action") == "cancellation":
                    continue
                counter[b["movie"]] += b.get("tickets", 0)
        return counter.most_common(top_n)

    def report_theater_occupancy(self, theater_name: str):
        theater = self.find_theater(theater_name)
        if not theater:
            raise ValueError("Theater not found.")
        occupancy = {}
        for t_str, available in theater.seats.items():
            # occupancy rate = (capacity - available) / capacity
            rate = (theater.capacity - available) / theater.capacity if theater.capacity else 0
            occupancy[t_str] = round(rate * 100, 2)
        return occupancy

    def recommend_for_user(self, username: str, top_n: int = 3):
        user = self.find_user(username)
        if not user:
            return []
        seen = {b['movie'] for b in user.booking_history if b.get('action') != 'cancellation'}
        # build global popularity
        pop = Counter()
        for u in self.users:
            for b in u.booking_history:
                if b.get('action') == 'cancellation':
                    continue
                pop[b['movie']] += b.get('tickets', 0)
        # recommend top popular movies the user hasn't seen
        recommendations = [movie for movie, _ in pop.most_common() if movie not in seen]
        return recommendations[:top_n]


# -------------------- Helper utilities for CLI --------------------
def input_datetime(prompt: str) -> datetime:
    while True:
        s = input(prompt).strip()
        try:
            return datetime.strptime(s, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format. Use YYYY-MM-DD HH:MM")


def create_default_admin(system: TicketSystem):
    if not any(u.role == 'admin' for u in system.users):
        admin = User('admin', 'admin123', role='admin')
        system.add_user(admin)
        print("Default admin user created -> username: admin, password: admin123")


# -------------------- CLI flows --------------------
def admin_menu(system: TicketSystem, current_user: User):
    while True:
        print("n--- Admin Menu ---")
        print("1. Add Theater")
        print("2. Add Movie to Theater")
        print("3. Display Theaters")
        print("4. Display Movies in Theater")
        print("5. View reports (popular movies, occupancy)")
        print("6. Logout")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            name = input("Enter theater name: ").strip()
            try:
                capacity = int(input("Enter theater capacity: ").strip())
            except ValueError:
                print("Invalid capacity"); continue
            try:
                system.add_theater(Theater(name, capacity))
                print("Theater added successfully!")
            except ValueError as e:
                print(e)
        elif choice == '2':
            t_name = input("Enter theater name: ").strip()
            theater = system.find_theater(t_name)
            if not theater:
                print("Theater not found."); continue
            title = input("Enter movie title: ").strip()
            try:
                duration = int(input("Enter movie duration (mins): ").strip())
            except ValueError:
                print("Invalid duration"); continue
            rating = input("Enter movie rating: ").strip()
            movie = Movie(title, duration, rating)
            st = input_datetime("Enter show time (YYYY-MM-DD HH:MM): ")
            movie.add_show_time(st)
            try:
                theater.add_movie(movie)
                # initialize seats for the show time
                theater.seats[Theater._time_str(st)] = theater.capacity
                print("Movie added successfully!")
            except ValueError as e:
                print(e)
        elif choice == '3':
            system.display_theaters()
        elif choice == '4':
            t_name = input("Enter theater name: ").strip()
            theater = system.find_theater(t_name)
            if theater:
                theater.display_movies()
            else:
                print("Theater not found.")
        elif choice == '5':
            print("n-- Most Popular Movies --")
            popular = system.report_most_popular_movies(10)
            for i, (movie, cnt) in enumerate(popular, 1):
                print(f"{i}. {movie} (tickets sold: {cnt})")
            tn = input("Enter theater name to view occupancy or press Enter to skip: ").strip()
            if tn:
                try:
                    occ = system.report_theater_occupancy(tn)
                    for tstr, rate in occ.items():
                        print(f"{tstr} -> {rate}% occupied")
                except ValueError as e:
                    print(e)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")


def customer_menu(system: TicketSystem, current_user: User):
    while True:
        print("n--- Customer Menu ---")
        print("1. View Theaters")
        print("2. View Movies in Theater")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. My Booking History")
        print("6. Recommendations")
        print("7. Logout")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            system.display_theaters()
        elif choice == '2':
            t_name = input("Enter theater name: ").strip()
            theater = system.find_theater(t_name)
            if theater:
                theater.display_movies()
            else:
                print("Theater not found.")
        elif choice == '3':
            t_name = input("Enter theater name: ").strip()
            theater = system.find_theater(t_name)
            if not theater:
                print("Theater not found."); continue
            movie_title = input("Enter movie title: ").strip()
            st = input_datetime("Enter show time (YYYY-MM-DD HH:MM): ")
            try:
                num_tickets = int(input("Enter number of tickets: ").strip())
            except ValueError:
                print("Invalid number"); continue
            try:
                ok = system.book(current_user.username, t_name, movie_title, st, num_tickets)
                if ok:
                    print("Tickets booked successfully!")
                else:
                    print("Not enough seats available.")
            except ValueError as e:
                print(e)
        elif choice == '4':
            t_name = input("Enter theater name: ").strip()
            theater = system.find_theater(t_name)
            if not theater:
                print("Theater not found."); continue
            movie_title = input("Enter movie title: ").strip()
            st = input_datetime("Enter show time (YYYY-MM-DD HH:MM): ")
            try:
                num_tickets = int(input("Enter number of tickets to cancel: ").strip())
            except ValueError:
                print("Invalid number"); continue
            try:
                if system.cancel(current_user.username, t_name, movie_title, st, num_tickets):
                    print("Booking cancelled.")
                else:
                    print("Could not cancel booking.")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print("n-- Your Booking History --")
            for b in current_user.booking_history:
                print(b)
        elif choice == '6':
            recs = system.recommend_for_user(current_user.username, top_n=5)
            if recs:
                print("Recommended movies for you:")
                for r in recs:
                    print("-", r)
            else:
                print("No recommendations available.")
        elif choice == '7':
            break
        else:
            print("Invalid choice.")


def register_flow(system: TicketSystem):
    print("n--- Register ---")
    username = input("Choose username: ").strip()
    if system.find_user(username):
        print("User already exists.")
        return None
    password = getpass.getpass("Choose a password: ") or input("Choose a password: ")
    role = 'customer'
    try:
        user = User(username, password, role=role)
        system.add_user(user)
        print("Registration successful. You can now login.")
        return user
    except ValueError as e:
        print(e)
        return None


def login_flow(system: TicketSystem):
    print("n--- Login ---")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ") or input("Password: ")
    try:
        user = system.authenticate(username, password)
        print(f"Welcome, {user.username} ({user.role})") 
        return user
    except ValueError:
        print("Invalid credentials.")
        return None


def main():
    system = TicketSystem()
    system.load_from_file()
    create_default_admin(system)

    while True:
        print("n=== Movie Ticket Management System ===n")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            user = login_flow(system)
            if not user:
                continue
            if user.role == 'admin':
                admin_menu(system, user)
            else:
                customer_menu(system, user)
            # save after each session
            system.save_to_file()
        elif choice == '2':
            register_flow(system)
            system.save_to_file()
        elif choice == '3':
            system.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()