import reflex as rx
from .state import AuthState


def index():
    return rx.fragment(on_mount=rx.redirect("/login"))


def login_page():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Login", size="8"),
                rx.input(
                    placeholder="Username",
                    value=AuthState.username,
                    on_change=AuthState.set_username,
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                    value=AuthState.password,
                    on_change=AuthState.set_password,
                ),
                rx.button("Login", on_click=AuthState.login),
                rx.text(AuthState.error, color="red"),
                rx.link("No account? Sign up", href="/signup"),
                spacing="4",
            ),
            padding="2em",
            width="25em",
        )
    )


def signup_page():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Signup", size="8"),
                rx.input(
                    placeholder="Username",
                    value=AuthState.username,
                    on_change=AuthState.set_username,
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                    value=AuthState.password,
                    on_change=AuthState.set_password,
                ),
                rx.button("Create Account", on_click=AuthState.sign_up),
                rx.text(AuthState.error, color="red"),
                rx.link("Already have an account? Login", href="/login"),
                spacing="4",
            ),
            padding="2em",
            width="25em",
        )
    )


def dashboard_page():
    # Redirect if not logged in
    AuthState.protect()

    return rx.center(
        rx.vstack(
            rx.heading(f"Welcome, {AuthState.username}! 🎉"),
            rx.button("Logout", on_click=AuthState.logout),
            spacing="4",
        )
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(login_page, route="/login")
app.add_page(signup_page, route="/signup")
app.add_page(dashboard_page, route="/dashboard")
app._compile()
