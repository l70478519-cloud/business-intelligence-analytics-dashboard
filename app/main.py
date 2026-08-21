from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
app=FastAPI(title="Business Intelligence API",version="0.1.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
class Metric(BaseModel):
    label: str = Field(min_length=2,max_length=120)
    value: str = Field(min_length=1,max_length=120)
records=[]
@app.get("/health")
def health(): return {"status":"ok","service":"business-intelligence-analytics-dashboard"}
@app.get("/api/metrics")
def list_records(): return records
@app.post("/api/metrics",status_code=201)
def create_record(record:Metric): records.append(record.model_dump()); return record
