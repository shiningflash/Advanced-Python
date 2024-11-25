import asyncio

async def low_priority_task():
    """Low priority task that repeatedly tries to run """
    while True:
        print("Low priority task running ...")
        await asyncio.sleep(1)

async def high_priority_task():
    """High priority task that dominates the event loop"""
    for _ in range (20):
        print("High priority task running ...")
        await asyncio.sleep(0.1)

async def main():
    await asyncio.gather(
        low_priority_task(),
        high_priority_task()
    )

asyncio.run(main())
