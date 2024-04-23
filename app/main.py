from model import *
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import slope_analysis as slope_analysis

app = FastAPI()

origins = [
    "null",
    "https://localhost:8000",
    "https://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/slope-graph")
async def slope_graph(landModel : LandModel):
    return HTMLResponse(slope_analysis.show_slope_graph().to_html())

@app.get("/")
async def root():
    return Response("OK")