from fasthtml.common import *

app, rt = fast_app()

setup_toasts(app)

def tt(s):
    add_toast(s,"test","info")

@rt("/toast")
def get(session):
    add_toast(session, "sdfsdf")

@rt('/toasting')
def get(session):
    # Normally one toast is enough, this allows us to see
    # different toast types in action.
    
    add_toast(session, f"Toast is being cooked", "info")
    add_toast(session, f"Toast is ready", "success")
    add_toast(session, f"Toast is getting a bit crispy", "warning")
    add_toast(session, f"Toast is burning!", "error")
    tt(session)
    return Titled("I like toast",P("get toast", hx_get="/toast", hx_swap="none"))

serve()