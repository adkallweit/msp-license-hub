from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio
from backend.worker import run_sync

scheduler = BlockingScheduler()

scheduler.add_job(
    lambda: asyncio.run(run_sync()),
    "cron",
    day=1,
    hour=2
)

scheduler.start()
