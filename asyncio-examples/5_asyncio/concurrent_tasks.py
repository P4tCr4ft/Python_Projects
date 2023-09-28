import asyncio
import time

# Extra Helper Functions
from asyncio import tasks
import pprint


# co-routine
async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def say_after2(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def say_after3(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def run():
    # Wraps co-routine in a task
    task1 = asyncio.create_task(say_after(1, "hello"))

    task2 = asyncio.create_task(say_after2(3, "world"))

    task3 = asyncio.create_task(say_after3(5, "more!"))

    print(f"started at {time.strftime('%X')}")

    # executes tasks concurrently
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    pprint.pprint(tasks.all_tasks(asyncio.get_event_loop()))
    # await task2
    # await task3

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(run(), debug=True)
