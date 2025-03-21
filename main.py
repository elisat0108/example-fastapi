from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Real Estate AI Tool API"}