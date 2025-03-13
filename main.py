from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest
from classes.Locker import Locker
from classes.LockerManager import LockerManager
#from classes.Reservation import Reservation

jd = Guest(0, "John Doe", "johndoe01@gmail.com", "012345678", "1234")

authService = AuthService()
authService.registerUser(jd)

lockerManager = LockerManager("lockers")
lockerManager.lockers.append(Locker(0,"Available",None,""))
lockerManager.lockers.append(Locker(1,"Available",None,""))
lockerManager.lockers.append(Locker(2,"Occupied", jd, ""))
lockerManager.lockers.append(Locker(3,"Under maintenance",None,""))
lockerManager.lockers.append(Locker(4,"Available",None,""))
lockerManager.lockers.append(Locker(5,"Available",None,""))


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


def lockerItem(id,status):
    return Div(H2("Locker"),H3(id), P(status), cls="locker")

def sidebar_buttons(role):
    match role:
        case "Guest":
            return [
                Div("Lockers",cls="sidebar-button"),
                Div("Payment",cls="sidebar-button"),
                Div("User Info", cls="sidebar-button")
            ]
        case "Maintenance":
            return [
                Div("User Info", cls="sidebar-button")
            ]
        case "Admin":
            return [
                Div("Lockers",cls="sidebar-button"),
                Div("Payment",cls="sidebar-button"),
                Div("User Info", cls="sidebar-button"),
                Div("Add Locker",cls='sidebar-button'),
                Div("Remove Locker",cls='sidebar-button'),
                Div("Edit Locker",cls='sidebar-button'),
            ]

@rt("/dashboard")
def get():
    return Main(
        Nav(H1("Hello")),
        Div(
            Div(
                *sidebar_buttons("Admin"),
            id="sidebar"),
            Div(
                *[lockerItem(locker.number, locker.status) for locker in lockerManager.lockers],
            id="main-dashboard"),
            
        id="dashboard-container"),
    style="padding:0")

@rt("/maintenance")
def get():
    return Titled("TLC Maintenance", P("maintenance"))

serve()