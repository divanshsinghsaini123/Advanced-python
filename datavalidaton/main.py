from pydantic import BaseModel  , EmailStr , Field , field_validator , computed_field
from fastapi import FastAPI , Depends
from fastapi.responses import JSONResponse
from Processing import loaddata


# Initialize the app
app = FastAPI()
class UserInput(BaseModel):
    id : int = Field(..., gt=0 , description="ID Must required")
    name : str = Field(...,min_length = 1 , max_length = 50 , json_schema_extra={"hint": "Use your full name"})
    email : EmailStr 
    age : int = Field(... , ge=18, le=100)

    # now i need to add some field validator 
    #iske liye hm use krenge inbuild decorator 
    @field_validator('name')
    @classmethod
    def name_mst_notempty(cls , v:str )-> str:
        tname = v.strip();
        if tname == "":
            raise ValueError('Name cannot be empty or just whitespace. Please enter a name.')
        return tname 
    
    @computed_field
    @property
    def is_adult(self)-> bool:
        return self.age >= 20
    #ek baat dekho ye krke isko diict me convert bhi nhi krna pda , 
    #pydentic ke andr sidha hi add kr diya isne 

#we need to create on more model for user output 
class UserOutput(BaseModel):
    id : int = Field(..., gt=0 , description="ID Must required")
    name : str = Field(...,min_length = 1 , max_length = 50 , json_schema_extra={"hint": "Use your full name"})
    email : EmailStr 
    age : int = Field(... , ge=18, le=100)
    is_adult: bool


@app.get("/")
async def Getallusers(data = Depends(loaddata) ):
    # data = await loaddata()
    return JSONResponse(
        status_code=200,
        content={"data": data, "message": "Created successfully"}
    )


@app.post("/users")
def create_user(user: UserInput):
    # final = user.model_dump()
    # is_adult = user.age >= 18
    # final["is_adult"] = is_adult
    return JSONResponse(
       
        content= {
            "user" : user.model_dump()
        }
    )
    # return user 

    




