from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest

authService = AuthService()

authService.registerUser(Guest(0, "John Doe", "johndoe01@gmail.com", "012345678", "1234"))




app, rt = fast_app(live=True, pico=True, hdrs=(Link(rel='stylesheet', href='stylesheet.css', type='text/css'),None)) #added ,None to make a tuple

@rt("/")
def get():
    return Titled("The Locker Company", 
            P("Welcome!"),   
            Form(
                Input(type="text", name="email"),
                Input(type="password", name="password"),
                Button("Login"),
                hx_post="/login", hx_target="#dashboard", hx_swap="innerHTML"
            ),
            Div(id="dashboard")
        )


@rt("/login")
def post(email:str, password:str):
    result = authService.loginUser(email,password)
    return result


def lockerItem():
    return Div(H2("Locker"),P("1"))


@rt("/dashboard")
def get():
    return Main(
        Nav(H1("Hello")),
        Div(
            Div(
                *[Div("button", style="padding: 0.5rem") for _ in range(5)],
            id="sidebar"),
            Div(
                *[lockerItem() for _ in range(5)],
            id="main-dashboard"),
            
        id="dashboard-container"),
    style="padding:0")

@rt("/maintenance")
def get():
    return Titled("TLC Maintenance", P("maintenance"))

serve()