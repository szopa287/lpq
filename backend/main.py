from fastapi import FastAPI

app = FastAPI()

@app.get("/api/test")
def read_root():
    return {"message": "fastapi dziala"}