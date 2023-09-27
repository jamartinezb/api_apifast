#swagger http://127.0.0.1:8000/docs
#uvicorn main:app --reload

from fastapi import FastAPI
from routers import users, products, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app =  FastAPI()
#routers

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url": "https://www.youtube.com/watch?v=_y9qQZXE24A",
            "codigo": "1234"}
    
