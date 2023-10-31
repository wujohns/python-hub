from fastapi import FastAPI
import asyncio

app = FastAPI()

async def check():
  while True:
    print('check-----')
    await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.create_task(check())

@app.get('/')
async def root():
  return { 'message': 'Hello' }

if __name__ == '__main__':
  import uvicorn
  uvicorn.run("asyncio-fastapi:app", host="0.0.0.0", port=5000, reload=True)
