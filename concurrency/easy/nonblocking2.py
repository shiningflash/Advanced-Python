import asyncio

counter = 0
lock = asyncio.Lock()

async def async_task_with_race(number: int):
    global counter
    
    """
    With Lock:
    Task 1 done. Counter 10000.
    Task 2 done. Counter 20000.
    Task 3 done. Counter 30000.
    
    Without Lock:
    Task 1 done. Counter 29998.
    Task 2 done. Counter 29999.
    Task 3 done. Counter 30000.
    """
    async with lock:
        for _ in range(10000):
            await asyncio.sleep(0.00001)
            counter += 1
    print(f"Task {number} done. Counter {counter}.")

async def main_with_lock():
    await asyncio.gather(async_task_with_race(1), async_task_with_race(2), async_task_with_race(3))
    
asyncio.run(main_with_lock())
