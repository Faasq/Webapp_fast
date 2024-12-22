from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import List
import uvicorn
app = FastAPI()
class Se(BaseModel):
    A : List[List[int]]
    B : List[List[int]]
    i : int
    j : int

    
mdata = {
   "A":[[1,2],[3,4]],
   "B":[[3,4],[5,6]],
   "i":0,
   "j":0 
}
A = mdata["A"]
B = mdata["B"]
i = mdata["i"]
j = mdata["j"]

app.count = 0

@app.get("/")
def read_root():
    app.count += 1
    print(app.count)
    return {"Hello": "World"}

@app.get("/Ka")
def Ka():
    return mdata

@app.get("/Kx")
def Kx():
    Sum = 0
    for r in range(len(A[i])):
        Sum=Sum+A[i][r]*B[r][j]
                
    
    return f'Answer is :{Sum}'

@app.post("/Ko")
def Ko(sea:Se):
    A = sea.A
    B = sea.B
    i = sea.i
    j = sea.j

    Sum = 0
    for r in range(len(A[i])):
        Sum=Sum+A[i][r]*B[r][j]
                
    
    return f'Answer is :{Sum}'



uvicorn.run(app,host ="0.0.0.0",port = 3000)
