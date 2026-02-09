# backend/src/server.py

from fastapi import FastAPI
from src.api.sessions import router as session_router
from src.api.npcs import router as npc_router
from src.api.plots import router as plot_router

app = FastAPI(title="RPG Living World Engine")

app.include_router(session_router, prefix="/sessions")
app.include_router(npc_router, prefix="/npcs")
app.include_router(plot_router, prefix="/plots")

@app.get("/")
def health():
    return {"status": "running"}
