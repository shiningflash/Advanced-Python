import asyncio

lock1 = asyncio.Lock()
lock2 = asyncio.Lock()

async def task1():
    print("Task 1: Waiting for Lock 1 and Lock 2")
    async with lock1:
        await asyncio.sleep(3)
        async with lock2:
            print("Task 1: Acquired lock 1 and lock 2")

async def task2():
    print("Task 2: Waiting for Lock 1 and Lock 2")
    async with lock2:
        await asyncio.sleep(2)
        async with lock1:
            print("Task 2: Acquired lock 1 and lock 2")

async def main():
    await asyncio.gather(task1(), task2())

async def async_main():
    try:
        await asyncio.wait_for(main(), timeout=5)
    except asyncio.TimeoutError:
        print("Deadlock detected!")
    
asyncio.run(async_main())