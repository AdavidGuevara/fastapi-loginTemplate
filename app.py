from fastapi import FastAPI
from routes.user_route import user

app = FastAPI(
    title="Login API",
    description="a login REST API using python and mysql",
    version="0.0.1"
)

app.include_router(user)
