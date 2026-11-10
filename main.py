from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from routers import patterns, auth
import crud

# 1. Create database tables (if they don't exist)
models.Base.metadata.create_all(bind=engine)

# 2. Initialize the FastAPI app
app = FastAPI(title="Patterns API", version="0.1.0")

# 3. Set up Jinja2 to look in the 'templates' folder
templates = Jinja2Templates(directory="templates")

# 4. Include our API routers
app.include_router(patterns.router)
app.include_router(auth.router)

# 5. Route: Homepage (Shows the patterns)
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    patterns_list = crud.get_patterns(db)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"patterns": patterns_list}
    )

# 6. Route: Login Page
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

# 7. Route: Signup Page
@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={}
    )