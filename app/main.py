from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI()

class OutputFormat(str, Enum):
    report = "Report"
    demo = "Demo"
    report_demo = "Both Report and Demo"

class QueryParams(BaseModel):
    query: str = Query(..., description="The query about FYP")
    output_format: OutputFormat = Query(..., description="What is the type of output.")

def get_query_params(query: str = Query(..., description="The query about FYP"), 
                     output_format: OutputFormat = Query(..., description="What is the type of output.")) -> QueryParams:
    return QueryParams(query=query, output_format=output_format)

@app.post('/query')
def query(params: QueryParams = Depends(get_query_params)):
    result = "details of FYP"
    return {"result": result, "query": params.dict()}

@app.get('/')
def home():
    return {"Detail": "Server is Working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
