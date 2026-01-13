from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def temp():
    return {"message" : "whhehere"}
    
