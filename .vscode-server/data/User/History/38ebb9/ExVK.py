
#///script
# This is the file for project P1
# script for building server requires --
# python 3.13 with dependencies of fastapi, uvicorn, requests
#///

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add.middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['GET', 'POST'],
    allow_headers = ['*']
)

#dummy endpoint
@app.get ("/")
def home():
    return {"Hello you are safe"}

@app.get ("/read")
def read_file(path:str):
    try :
        with open(path,"r") as f:
            return f.read
    except Exception as e:
          
    return {"Hello you are safe"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run (app,host="0.0.0.0", port = 8000)


