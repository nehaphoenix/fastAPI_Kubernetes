#import statements
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

#Pydantic Base model class
class OKR(BaseModel):
  '''
  Class module to store OKRs
  '''
  Objective: str
  due_date: str
  completion_percentage: int
  KeyResults: str

app = FastAPI(title="OKR API")

# Functions to Create, Read, Update and Delete OKR's.
store_okr = []

@app.get('/')
async def home():
  '''
  Base function to display OKR board message on root url '/'
  :return: Message to user
  '''
  return {"Message": "OKR board"}

@app.post('/okr/')
async def create_okr(okr: OKR):
  '''
  "Post" function to create OKRs.
  :param okr: class
  :return: json response with class attributes containing okr and due_date.
  '''
  store_okr.append(okr)
  return okr

@app.get('/okr/', response_model=List[OKR])
async def get_all_okrs():
  '''
  "get" function to display all OKRs.
  :return: json response with class attributes for every OKR created.
  '''
  return store_okr

@app.get('/okr/{id}')
async def get_okr(id: int):
  '''
  "get" function to fetch particular OKR using "id" as param.
  :param id: integer
  :return: json response with class attributes for particular okr.
  '''
  try:
    return store_okr[id]
  except:
    raise HTTPException(status_code=404, detail="OKR Not Found")

@app.put('/okr/{id}')
async def update_okr(id: int, okr: OKR):
  '''
  "put" function to update the existing OKR.
  :param id: integer
  :param okr: class
  :return: updated json response with class attributes for particular okr.
  '''
  try:
    store_okr[id] = okr
    return store_okr[id]
  except:
    raise HTTPException(status_code=404, detail="okr Not Found")

@app.delete('/okr/{id}')
async def delete_okr(id: int):
  '''
  "delete" function to delete particular okr.
  :param id: integer
  :return: json response for deleted okr.
  '''
  try:
    obj = store_okr[id]
    store_okr.pop(id)
    return obj
  except:
    raise HTTPException(status_code=404, detail="OKR Not Found")