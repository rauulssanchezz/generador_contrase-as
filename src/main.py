
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.generate_password_router import router as generate_router

app = FastAPI(
    title='Password Generator'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_router)
