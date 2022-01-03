import asyncio
import time



async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)



## Version 1
async def main_v1():
    print(f"start at {time.strftime('%X')}")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print(f"finish at {time.strftime('%X')}")


## Version 2
async def main_v2():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(say_after(2, "Hello"))
    task2 = loop.create_task(say_after(1, "World"))

    print(f"start at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finish at {time.strftime('%X')}")



loop = asyncio.get_event_loop()
print("main_v1:")
result = loop.run_until_complete(main_v1())
print("main_v2:")
result = loop.run_until_complete(main_v2())