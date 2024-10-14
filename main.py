from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.registration import route as registration
from src.auth.log_in_out import route as log_in_out
from src.product_endpoint import route as product

app = FastAPI()

origins = [
    'http://127.0.0.1:8000',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(registration)
app.include_router(log_in_out)
app.include_router(product)