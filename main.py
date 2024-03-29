from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):

     at.bar1.custom.data = [{"x":2010, "category1":40, "category2":50}, 
                           {"x":2011, "category1":30, "category2":60}]

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass