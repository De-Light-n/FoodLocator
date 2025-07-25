from fastapi import FastAPI
import uvicorn

from config import config 
from routes import auth, restaurants

app = FastAPI()

app.include_router(auth.router, tags=["auth"], prefix="/api")
app.include_router(restaurants.router, tags=["restaurants"], prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.APP_HOST, port=config.APP_PORT, reload=True)