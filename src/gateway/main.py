import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
async def testApp():
    return {"Hello": "FastAPI!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)