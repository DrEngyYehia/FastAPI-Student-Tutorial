
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create the FastAPI application
app = FastAPI()

# Make CSS and images accessible to the browser
app.mount("/static", StaticFiles(directory="static"), name="static")

# Specify the folder containing HTML templates
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


# About Us page
@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )


# Contact Us page
@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={}
    )


# Menu page
@app.get("/menu")
def menu(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="menu.html",
        context={}
    )
