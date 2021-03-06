import uvicorn
from config import PORT

if __name__ == '__main__':
    uvicorn.run("tutorial:app", host = '127.0.0.1', port = int(PORT), reload = True, debug = True, workers = 1)