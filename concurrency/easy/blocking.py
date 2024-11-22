import asyncio
import time


async def async_task(number: int):
    print(f"Start async task {number}")
    time.sleep(3)  # blocking call
    print(f"End async task {number}")

async def main():
    """
    Output
    -
    Start async task 1
    End async task 1
    Start async task 2
    End async task 2
    Start async task 3
    End async task 3
    
    Time needed: 9.01
    """
    start_time = time.time()
    await asyncio.gather(async_task(1), async_task(2), async_task(3))
    end_time = time.time()
    print(f"\nTime needed: {round((end_time-start_time), 2)}")
    
asyncio.run(main())
