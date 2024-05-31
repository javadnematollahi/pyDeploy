import time
import random
import asyncio

async def get():
    print("get started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"get ended in {r} second")

def extract():
    print("extract started")
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"extract ended in {r} second")

async def download():
    print("download started")
    await asyncio.create_task(get())
    r = random.randint(0, 10)
    extract()
    await asyncio.sleep(r)
    print(f"download ended in {r} second")


async def printer():
    print("printer started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"printer ended in {r} second")


async def ai_video():
    print("ai_video started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"ai_video enden in {r} second")


async def ai_audio():
    print("ai_audio started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"ai_audio enden in {r} second")


def mix():
    print("mix started")
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"mix enden in {r} second")

async def ai():
    print("AI started")
    await asyncio.gather(ai_audio(),ai_video())
    mix()
    r = random.randint(0, 10)
    print(f"AI enden in {r} second")


async def main():
    await asyncio.gather(download(), printer(), ai())
    print("Main ended")

if __name__=="__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")
