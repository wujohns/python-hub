from fastapi import FastAPI
import asyncio
import asyncio_importmm

app = FastAPI()

async def check():
  while True:
    print('check-----')
    await asyncio.sleep(1)

# 这里使用 asyncio.new_event_loop() 会导致错乱，主要原因为 app = FastAPI() 已经创建了对应的 loop
loop = asyncio.get_event_loop()
loop.create_task(check())
loop.create_task(asyncio_importmm.init())

@app.get('/')
async def root():
  return { 'message': 'Hello' }

if __name__ == '__main__':
  import uvicorn
  uvicorn.run("asyncio-fastapi:app", host="0.0.0.0", port=5000, reload=True)
