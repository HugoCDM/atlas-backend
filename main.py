from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.supabase_tables import router

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'https://dynamic-trifle-a949c7.netlify.app/'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'])


