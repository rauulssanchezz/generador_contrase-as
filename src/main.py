from fastapi import FastAPI
from src.routers.generate_password_router import router as generate_router

app = FastAPI(
    title='Password Generator'
)

app.include_router(generate_router)
