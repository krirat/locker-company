from fasthtml.common import *
import datetime








app, rt = fast_app(live=True)

@rt("/")
def get():
    return Titled("The Locker Company", P("Welcome!"))

@rt("/admin")
def get():
    return Titled("TLC Admin", P("admin"))

@rt("/maintenance")
def get():
    return Titled("TLC Maintenance", P("maintenance"))

serve()