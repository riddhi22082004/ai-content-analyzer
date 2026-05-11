from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.api.routes import router


app = FastAPI(
    title="AI Website Intelligence API"
)


# CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ROUTES

app.include_router(router)


@app.get("/")
def root():

    return {

        "message":
        "AI Website Intelligence API Running"
    }