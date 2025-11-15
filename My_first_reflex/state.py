import reflex as rx

users_db = {}


class AuthState(rx.State):
    username: str = ""
    password: str = ""
    error: str = ""
    logged_in: bool = False

    def sign_up(self):
        if self.username in users_db:
            self.error = "Username already exists."
            return

        users_db[self.username] = self.password
        self.logged_in = True
        return rx.redirect("/dashboard")

    def login(self):
        if self.username not in users_db:
            self.error = "User not found."
            return

        if users_db[self.username] != self.password:
            self.error = "Incorrect password."
            return

        self.logged_in = True
        return rx.redirect("/dashboard")

    def logout(self):
        self.logged_in = False
        self.username = ""
        self.password = ""
        return rx.redirect("/login")

    def protect(self):
        if not self.logged_in:
            return rx.redirect("/login")
