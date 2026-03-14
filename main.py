from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/dummy")
def get_dummy():
    return {"message": "This is a dummy endpoint", "data": [1, 2, 3, 4, 5]}

@app.post("/dummy")
def create_dummy(item: dict):
    return {"created": item}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)