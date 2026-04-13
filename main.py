from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.supabase_tables import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5173',
        'http://localhost:5500',
        'http://127.0.0.1:5500',
        'http://localhost:3000',
        'https://stately-treacle-e466de.netlify.app',
        'https://praca11.netlify.app'
    ],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'])

app.include_router(router)


