from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.Guest import Guest
from classes.Locker import Locker
from classes.LockerManager import LockerManager
from classes.Admin import Admin
from classes.Maintenance import Maintenance
#from classes.Reservation import Reservation

authService = AuthService()
lockerManager = LockerManager("lockers")

jd = Guest("John Doe", "johndoe01@gmail.com", "012345678", "1234")
admin = Admin("admin", "admin", "", "admin")
mt = Maintenance("maintenance", "maintenance", "", "1234")
authService.registerUser(jd)
authService.registerUser(admin)
authService.registerUser(mt)
lockerManager.lockers.append(Locker(0,"Available",None,""))
lockerManager.lockers.append(Locker(1,"Available",None,""))
lockerManager.lockers.append(Locker(2,"Occupied", jd, ""))
lockerManager.lockers.append(Locker(3,"Under maintenance",None,""))
lockerManager.lockers.append(Locker(4,"Available",None,""))
lockerManager.lockers.append(Locker(5,"Available",None,""))


app, rt = fast_app(hdrs=(Link(rel='stylesheet', href='stylesheet.css', type='text/css'),None)) #added ,None to make a tuple

currentUser = None



@rt("/")
def get():
    return loginPage()

@rt("/")
def post(email:str, password:str):
    user = authService.loginUser(email,password)

    if user:
        global currentUser
        currentUser = user
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
    global currentUser
    currentUser = newUser
    return dashboard(newUser)


@rt("/userinfo")
def post(name:str, email:str, phone:str):
    return Div(
                P(name),
                P(email),
                P(phone), 
            )

@rt("/reservelocker/{id}")
def get(id:int):
    locker = lockerManager.get_locker_by_number(id)
    lockerManager.assign_locker_to_user(locker, currentUser)
    locker.set_pin("1234")
    return Div(
        H1("Reservation Successful"),
        P(f"Your PIN is: {locker.get_pin()}"),
        P("Have a good day!"),
    )

@rt("/lockers")
def get():
    return Div(

    )

@rt("/refresh")
def get():
    return [lockerItem(number, locker.status) if locker.isAvailable() else None for number, locker in enumerate(lockerManager.lockers)]
    
     
# ------ Components -----------------------

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
        
def dashboard(user):

    return Main(
                Nav(
                     H1(f"Hello, {user.name}"), 
                     A("Log Out", href="/")
                ),
                Div(
                    Div(
                        *sidebarButtons(user),
                        id="sidebar"
                    ),
                    Div(
                        *[lockerItem(number, locker.status) if locker.isAvailable() else None for number, locker in enumerate(lockerManager.lockers)],
                        id="main-dashboard",hx_get="/refresh"
                    ),
                    id="dashboard-container"
                ),
                Div(
                    Div(cls="modal-content"),
                    id="modal"
                ),
            style="padding:0"
            )

def sidebarButtons(user):

    if type(user) == Admin:
        return [

            Script('''
        
        function closeModal(){
                let modal = document.getElementById("modal")
                modal.removeAttribute("class")
        }
        function openModal(){
                let modal = document.getElementById("modal")
                modal.setAttribute("class","active")
                modal.addEventListener("click",closeModal)
        }
        var buttons = document.getElementsByClassName("sidebar-button")
        for (var button of buttons) {
                 button.addEventListener("click", openModal)
        }
    '''),

            Div("Lockers",cls="sidebar-button",hx_post="/lockers", hx_target=".modal"),
            Div("Payment",cls="sidebar-button"),
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal-content"),
            Div("Add Locker",cls='sidebar-button'),
            Div("Remove Locker",cls='sidebar-button'),
            Div("Edit Locker",cls='sidebar-button'),
        ]
    
    if type(user) == Maintenance:
        return [

            Script('''
        
        function closeModal(){
                let modal = document.getElementById("modal")
                modal.removeAttribute("class")
        }
        function openModal(){
                let modal = document.getElementById("modal")
                modal.setAttribute("class","active")
                modal.addEventListener("click",closeModal)
        }
        var buttons = document.getElementsByClassName("sidebar-button")
        for (var button of buttons) {
                 button.addEventListener("click", openModal)
        }
    '''),
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal-content"),
        ]
    
    if type(user) == Guest:
        return [

            Script('''
        
        function closeModal(){
                let modal = document.getElementById("modal")
                modal.removeAttribute("class")
        }
        function openModal(){
                let modal = document.getElementById("modal")
                modal.setAttribute("class","active")
                modal.addEventListener("click",closeModal)
        }
        var buttons = document.getElementsByClassName("sidebar-button")
        for (var button of buttons) {
                 button.addEventListener("click", openModal)
        }
    '''),
            Div("Lockers",cls="sidebar-button",hx_post="/lockers", hx_vals="user:user"),
            Div("Payment",cls="sidebar-button"),
            Div("User Info", cls="sidebar-button",hx_post="/userinfo", hx_vals=f'{{"name": "{user.name}", "email": "{user.email}", "phone": "{user.phone}"}}',hx_target=".modal-content"),
            
        ]
    
def lockerItem(id,status):

    return Div(
         H2("Locker"),
         H3(id), 
         P(status), 
         Script('''
        
        function closeModal(){
                let modal = document.getElementById("modal")
                modal.removeAttribute("class")
        }
        function openModal(){
                let modal = document.getElementById("modal")
                modal.setAttribute("class","active")
                modal.addEventListener("click",closeModal)
        }
        var buttons = document.getElementsByClassName("locker")
        for (var button of buttons) {
                 button.addEventListener("click", openModal)
        }
    '''),
         cls=f"locker {id}",
         hx_get=f"/reservelocker/{id}",
         hx_target=".modal-content"

    )



serve()