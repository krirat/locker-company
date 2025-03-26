from fasthtml.common import *
import datetime
from classes.AuthService import AuthService
from classes.ActivityLog import ActivityLog
from classes.Guest import Guest
from classes.Locker import Locker
from classes.LockerManager import LockerManager
from classes.Admin import Admin
from classes.Maintenance import Maintenance
from classes.PaymentProcessor import PaymentProcessor

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
lockerManager.lockers.append(Locker(2,"Available", None, ""))
lockerManager.lockers.append(Locker(3,"Available",None,""))
lockerManager.lockers.append(Locker(4,"Available",None,""))
lockerManager.lockers.append(Locker(5,"Available",None,""))




app, rt = fast_app(hdrs=[Link(rel='stylesheet', href='stylesheet.css', type='text/css')])

currentUser = None

@rt("/")
def get():
    return loginPage()

@rt("/")
def post(session, email:str, password:str):
    user = authService.loginUser(email,password)
    
    if user:
        session['user'] = user
        global currentUser
        currentUser = user
        activityLog.log_event(user,None,"Login",datetime.datetime.now())
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
    locker.set_pin("1234") #TODO: randomize number
    activityLog.log_event(currentUser,locker,"Reserve",datetime.datetime.now())

    return Div(
                H1("Reservation Successful"),
                P(f"Your PIN is: {locker.get_pin()}"),
                P("Have a good day!"),
                
            )

@rt("/open/{id}")
def get(id: int): #TODO: use javascript instead
    return Div(
        Form(
            Input(type="text", name="pin", placeholder = "Your PIN Number (6 Digits)"),
            Input(type="submit"),
            hx_post=f"/open/{id}",
            hx_target="#main-dashboard"
        ),
        
    )

@rt("/open/{id}")
def post(id: int, pin: str):
    locker = lockerManager.get_locker_by_number(id)
    if locker and locker.get_pin() == pin:
        lockerManager.release_locker(locker)
        activityLog.log_event(currentUser,locker,"Cancelled Reservation",datetime.datetime.now())
        return myLockerList()
    

    
    
@rt("/lockers")
def get():
    return lockerList()

@rt("/mylockers")
def get():
    return myLockerList()

@rt("/lockerinfo/{id}")
def get():
    return Div(

    )

# @rt("/payment")
# def get():
#     return Div(
#         A("Topup",href="/add_money"))

# @rt("/add_money")
# def get():
#     return Form(
#         Fieldset(
#             Input(
#                 type="text",
#                 money="text",
#                 placeholder="Enter_amount",
#                 required=True,
#                 maxlength = 10,
#             ),
#             Button("Submit", type="submit"),
#             role="group",
#         ),)

@rt("/payment")
def get():
    return Div(
        P("Balance: " + str(currentUser.balance)),
        P("Top Up"),
        Form(
            Input(type="number", name = "amount", placeholder ="Enter amount"),
            Input(type="submit", value = "Top up"),
            hx_post="/payment/topup",
            hx_target="#main-dashboard",
            
        ),
        P("Make a payment"),
        Form(
            Input(type="number", name="amount", placeholder="Enter amount to pay"),
            Input(type="submit", value="Pay"),
            hx_post="/payment/process",
            hx_target="#main-dashboard"
        )
    )

@rt("/payment/topup")
def post(amount : float):
    PaymentProcessor.top_up_account(currentUser, amount)
    return Div(
        P(f"Account topped up by {amount}. New balance: {currentUser.balance}")
    )

@rt("/payment/process")
def post(amount : float):
    PaymentProcessor.process_payment(currentUser, amount)
    if currentUser.balance >= amount:
        return Div(
            P(f"Payment of {amount} processed. New balance: {currentUser.balance}")
        )
    else:
        return Div(
            P(f"Insufficient balance to process payment of {amount}.")
        )


@rt("/userinfo")
def get():
    return Div(
                P("Name: " + currentUser.name),
                P("Email: " + currentUser.email),
                P("Phone no.: " + currentUser.phone), 
                P("Balance: " + str(currentUser.balance))
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

@rt("/logs")
def get():
    logs = activityLog.get_logs()
    logList = []
    for log in logs:
        logList.append(Li(f"{log.user.name} {" => Locker: " + str(log.locker.number) if log.locker else ""} | {log.action} at {log.timestamp} "))

    return Ul(*logList)
    

    
# ------ Components -----------------------

def loginPage():

    return Titled("The Locker Company", 
                P("Welcome!"),   
                Form(
                    Input(type="text", name="email", placeholder = "Email"),
                    Input(type="password", name="password", placeholder = "Password"),
                    Button("Login", id="login"),
                    hx_post="/", hx_target="body", id="login-form"
                ),
                #P("Register", id="register", hx_get="/register", hx_target="body"),
                A("Register", id="register", href="/register"),
            )

def registerPage():

    return Titled("The Locker Company", 
                P("Welcome!"),

                Form(
                    Input(type="text", name="name", placeholder = "Name"),
                    Input(type="email", name="email", placeholder = "Email"),
                    Input(type="text", name="phone", placeholder = "Phone Numbebr"),
                    Input(type="text", name="password", placeholder = "Password"),
                    Button("Register", id="register"),
                    hx_post="/register", hx_target="body", id="register-form"
                ),
                #P("login", id="login", hx_get="/", hx_target="body"),
                A("login", id="login", href="/"),
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
                        *lockerList(),
                        id="main-dashboard",
                    ),
                    id="dashboard-container"
                ),
                Div(
                    Div(cls="modal-content"),
                    Button("Close",id="close"),
                    id="modal"
                ),
                style="padding:0"
            )

def sidebarButtons(user):

    if type(user) == Admin:
        return [
            Div("Lockers", cls="sidebar-button", hx_get="/lockers", hx_target="#main-dashboard"),
            Div("My Lockers", cls="sidebar-button", hx_get="/mylockers", hx_target="#main-dashboard"),
            Div("User Info", cls="sidebar-button", hx_get="/userinfo", hx_target="#main-dashboard"),
            Div("Payment", cls="sidebar-button", hx_get="/payment", hx_target="#main-dashboard"),
            Div("Add Locker", cls='sidebar-button', hx_get="/addlocker", hx_target="#main-dashboard"),
            Div("Remove Locker", cls='sidebar-button', hx_get="/removelocker", hx_target="#main-dashboard"),
            Div("Logs", cls='sidebar-button', hx_get="/logs", hx_target="#main-dashboard"),
        ] 
    
    if type(user) == Maintenance:
        return [
            Div("Lockers", cls="sidebar-button", hx_get="/lockers", hx_target="#main-dashboard"),
            Div("My Lockers", cls="sidebar-button", hx_get="/mylockers", hx_target="#main-dashboard"),
            Div("User Info", cls="sidebar-button",hx_get="/userinfo", hx_target="#main-dashboard"),
            Div("Payment", cls="sidebar-button", hx_get="/payment", hx_target="#main-dashboard"),
            Div("Perform Maintenance", cls='sidebar-button', hx_get="/maintenance/perform", hx_target="#main-dashboard"),
            Div("Check Lockers", cls='sidebar-button', hx_get="/maintenance/check", hx_target="#main-dashboard"),
            Div("Update Locker Status", cls='sidebar-button', hx_post="/maintenance/update", hx_target="#main-dashboard"),
        ]
    
    if type(user) == Guest:
        return [
            Div("Lockers", cls="sidebar-button", hx_get="/lockers", hx_target="#main-dashboard"),
            Div("My Lockers", cls="sidebar-button", hx_get="/mylockers", hx_target="#main-dashboard"),
            Div("User Info", cls="sidebar-button", hx_get="/userinfo", hx_target="#main-dashboard"),     
            Div("Payment", cls="sidebar-button", hx_get="/payment", hx_target="#main-dashboard"),
        ]
    
def lockerList():
    _lockerList = []

    for number, locker in enumerate(lockerManager.lockers):
        if locker.isAvailable():
            _lockerList.append(lockerItem(number, locker.status, hx_get=f"/reserve/{number}", hx_target=".modal-content"))

    return _lockerList

def myLockerList():
    _myLockerList = []

    for number, locker in enumerate(lockerManager.lockers):
        if not locker.isAvailable() and locker.assignedUser == currentUser:
            _myLockerList.append(lockerItem(number, locker.status, hx_get=f"/open/{number}", hx_target=".modal-content"))
    
    return _myLockerList

    
def lockerItem(id,status, **kwargs):

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
                    let close = document.getElementById("close")
                    modal.setAttribute("class","active")
                    button.removeEventListener("click", openModal)
                    close.addEventListener("click",closeModal)
            }
            var buttons = document.getElementsByClassName("locker")
            for (var button of buttons) {
                    button.addEventListener("click", openModal)
            }
                
        '''),

        cls=f"locker {id}",
        **kwargs,
    )



serve()