import asyncio

async def low_priority_task():
    """Low priority task that repeatedly tries to run """
    while True:
        print("Low priority task running ...")
        await asyncio.sleep(1)

async def medium_priority_task():
    while True:
        print("Medium-priority task running...")
        await asyncio.sleep(0.5)

async def high_priority_task():
    """High priority task that dominates the event loop"""
    for _ in range (20):
        print("High priority task running ...")
        await asyncio.sleep(0.1)
        await asyncio.sleep(0)

async def main():
    await asyncio.gather(
        low_priority_task(),
        medium_priority_task(),
        high_priority_task()
    )

asyncio.run(main())
