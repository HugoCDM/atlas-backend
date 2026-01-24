from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.supabase_tables import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'https://stately-treacle-e466de.netlify.app'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'])

@app.get('/')
async def health():
    return {'status': 'ok'}

app.include_router(router)


