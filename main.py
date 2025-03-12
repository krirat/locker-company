from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest

authService = AuthService()

authService.registerUser(Guest(0, "John Doe", "johndoe01@gmail.com", "012345678", "1234"))




app, rt = fast_app()

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



@rt("/dashboard")
def get():
    return Main(
        Titled("Hello")
    )

@rt("/maintenance")
def get():
    return Titled("TLC Maintenance", P("maintenance"))

serve()