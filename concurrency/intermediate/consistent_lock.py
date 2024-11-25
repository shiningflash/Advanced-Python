import asyncio

lock1 = asyncio.Lock()
lock2 = asyncio.Lock()

async def task1():
    print("Task 1: Waiting for Lock 1 and Lock 2")
    async with lock1:
        async with lock2:
            print("Task 1: Acquired lock 1 and lock 2")

async def task2():
    print("Task 2: Waiting for Lock 1 and Lock 2")
    async with lock1:
        async with lock2:
            print("Task 2: Acquired lock 1 and lock 2")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
