from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest
from classes.Locker import Locker
from classes.LockerManager import LockerManager
from classes.Admin import Admin
from classes.Maintenance import Maintenance
#from classes.Reservation import Reservation

jd = Guest("John Doe", "johndoe01@gmail.com", "012345678", "1234")
admin = Admin("admin", "admin", "", "admin")
mt = Maintenance("maintenance", "maintenance", "", "1234")


authService = AuthService()
authService.registerUser(jd)
authService.registerUser(admin)
authService.registerUser(mt)

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
    return loginPage()

@rt("/")
def post(email:str, password:str):
    user = authService.loginUser(email,password)

    if user:
        return dashboard(user)
    else:
        return loginPage()



@rt("/register")
def get():
    return registerPage()

@rt("/register")
def post(name:str, email:str, phone:str, password:str):
    newUser = Guest(name, email, phone, password)
    authService.registerUser(newUser)
    return dashboard(newUser)


@rt("/userinfo")
def post(name:str, email:str, phone:str):
    return Div(
         P(name),
         P(email),
         P(phone),
         
    )
     

def loginPage():
    return Titled("The Locker Company", 
            P("Welcome!"),   
            Form(
                Input(type="text", name="email"),
                Input(type="password", name="password"),
                Button("Login", id="login"),
                hx_post="/", hx_target="body", id="login-form"
            ),
            P("Register", id="register", hx_get="/register", hx_target="body"),
        )

def registerPage():
    return Titled("The Locker Company", 
            P("Welcome!"),   
            Form(
                Input(type="text", name="name"),
                Input(type="email", name="email"),
                Input(type="text", name="phone"),
                Input(type="text", name="password"),
                Button("Register", id="register"),
                hx_post="/register", hx_target="body", id="register-form"
            ),
            P("login", id="login", hx_get="/", hx_target="body"),
        )

def lockerItem(id,status):
    return Div(
         H2("Locker"),
         H3(id), 
         P(status), 
         cls="locker"
    )


def getLockerList():
     return H1("asfasdfas")


def sidebarButtons(user):
    if type(user) == Admin:
        return [
            Div("Lockers",cls="sidebar-button",hx_post="/lockers", hx_target=".modal"),
            Div("Payment",cls="sidebar-button"),
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal"),
            Div("Add Locker",cls='sidebar-button'),
            Div("Remove Locker",cls='sidebar-button'),
            Div("Edit Locker",cls='sidebar-button'),
        ]
    if type(user) == Maintenance:
        return [
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal"),
        ]
    if type(user) == Guest:
        return [
            Div("Lockers",cls="sidebar-button",hx_post="/lockers", hx_vals="user:user"),
            Div("Payment",cls="sidebar-button"),
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal"),
            
        ]
        



def dashboard(user):

    if type(user) == Admin:
            userType = "Admin"
    if type(user) == Maintenance:
            userType = "Maintenance"
    if type(user) == Guest:
            userType = "Guest"

    return Main(
        Nav(H1(f"Hello, {user.name}"), A("Log Out", href="/")),
        Div(
            Div(
                *sidebarButtons(user),
            id="sidebar"),
            Div(
                *[lockerItem(locker.number, locker.status) for locker in lockerManager.lockers],
            id="main-dashboard"),
            
        id="dashboard-container"),
        Div(cls="modal"),
    style="padding:0")


serve()