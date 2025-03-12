from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest

authService = AuthService()

authService.registerUser(Guest(0, "John Doe", "johndoe01@gmail.com", "012345678", "1234"))




app, rt = fast_app(live=True)

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
        Nav("Hello",    
        style="color:white; background-color:#2991c2; padding:32px"),
        Div(
            Div(
                *[Div("button", style="padding: 0.5rem") for _ in range(5)],
            id="sidebar", 
            style="background-color:#0c364a; flex-grow: 1; display:flex; flex-direction:column; padding: 1rem"),
            Div("content",
            
            id="main-dashboard",
            style="background-color: #dcedf5; flex-grow: 5; padding: 5rem"),
        style="display:flex; flex-direction:row; align-content: stretch; height: 100vh"),
    style="padding:0")

@rt("/maintenance")
def get():
    return Titled("TLC Maintenance", P("maintenance"))

serve()