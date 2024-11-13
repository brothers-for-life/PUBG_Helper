from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/maps", StaticFiles(directory="maps"), name="maps")

@app.get("/")
async def root():
    # Serve the main HTML page
    return FileResponse("index.html")
