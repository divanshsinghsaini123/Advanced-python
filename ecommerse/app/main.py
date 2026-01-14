from fastapi import FastAPI , request 
app = FastAPI()


@app.middleware("http")
def thisismiddlwear(request : request , call_next ):
    # yaha kutch bhi kro whatever you want 
    response = call_next(request) #ab ye gya nest bnde ke pass jo bhi crud krne hain vo sb kro
    # ab yaha se jane ka time ho gya 
    return response 
@app.get("/")
def temp():
    return {"message" : "whhehere"}
    
