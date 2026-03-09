from fastapi import FastAPI
from backend.worker import run_sync
import asyncio

app = FastAPI(title="MSP License Hub")

@app.get("/sync")

async def sync():

    await run_sync()

    return {"status": "sync finished"}
