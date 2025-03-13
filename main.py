from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.ActivityLog import ActivityLog
from classes.Guest import Guest
from classes.Locker import Locker
from classes.LockerManager import LockerManager
from classes.Admin import Admin
from classes.Maintenance import Maintenance

authService = AuthService()
lockerManager = LockerManager("lockers")
activityLog = ActivityLog()

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
        activityLog.log_event(user,None,"Login",datetime.datetime.now())
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
    activityLog.log_event(newUser,None,"Login",datetime.datetime.now())
    return dashboard(newUser)



@rt("/reserve/{id}")
def get(id:int):
    locker = lockerManager.get_locker_by_number(id)
    lockerManager.assign_locker_to_user(locker, currentUser)
    locker.set_pin("1234")
    activityLog.log_event(currentUser,locker,"Reserve",datetime.datetime.now())

    return Div(
                H1("Reservation Successful"),
                P(f"Your PIN is: {locker.get_pin()}"),
                P("Have a good day!"),
            )

@rt("/lockers")
def get():
    return lockerList()

@rt("/payment")
def get():
    return Div(
        P("moneyyy")
    )

@rt("/userinfo")
def get():
    return Div(
                P(currentUser.name),
                P(currentUser.email),
                P(currentUser.phone), 
            )

@rt("/addlocker")
def get():
    lockerManager.add_locker()
    activityLog.log_event(currentUser,None,"Add Locker",datetime.datetime.now())
    return lockerList()

@rt("/removelocker")
def get():
    lockerManager.remove_locker()
    activityLog.log_event(currentUser,None,"Remove Locker",datetime.datetime.now())
    return lockerList()

    
     
# ------ Components -----------------------

def lockerList():
    return [lockerItem(number, locker.status) if locker.isAvailable() else None for number, locker in enumerate(lockerManager.lockers)]

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
                        id="main-dashboard",hx_get="/lockers"
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
            Div("Lockers", cls="sidebar-button", hx_get="/lockers", hx_target="#main-dashboard"),
            Div("Payment", cls="sidebar-button", hx_get="/payment", hx_target="#main-dashboard"),
            Div("User Info", cls="sidebar-button", hx_get="/userinfo", hx_target="#main-dashboard"),
            Div("Add Locker", cls='sidebar-button', hx_get="/addlocker", hx_target="#main-dashboard"),
            Div("Remove Locker", cls='sidebar-button', hx_get="/removelocker", hx_target="#main-dashboard"),
            Div("Edit Locker", cls='sidebar-button', hx_get="/editlocker", hx_target="#main-dashboard"),
        ] 
    
    if type(user) == Maintenance:
        return [
            Div("User Info", cls="sidebar-button",hx_get="/userinfo", hx_target="#main-dashboard"),
        ]
    
    if type(user) == Guest:
        return [
            Div("Lockers", cls="sidebar-button", hx_get="/lockers", hx_target="#main-dashboard"),
            Div("Payment", cls="sidebar-button", hx_get="/payment", hx_target="#main-dashboard"),
            Div("User Info", cls="sidebar-button", hx_get="/userinfo", hx_target="#main-dashboard"),     
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
         hx_get=f"/reserve/{id}",
         hx_target=".modal-content"

    )



serve()