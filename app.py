from fastapi import FastAPI, File, UploadFile
import uvicorn
from pydantic import BaseModel
from fastapi_frame_stream import FrameStreamer
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
fs = FrameStreamer()


origins = [
    "http://localhost:63342",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputImg(BaseModel):
    img_base64str: str


@app.post("/send_frame_from_string/{stream_id}")
async def send_frame_from_string(stream_id: str, d: InputImg):
    await fs.send_frame(stream_id, d.img_base64str)


@app.post("/send_frame_from_file/{stream_id}")
async def send_frame_from_file(stream_id: str, file: UploadFile = File(...)):
    await fs.send_frame(stream_id, file)


@app.get("/video_feed/{stream_id}")
async def video_feed(stream_id: str):
    return fs.get_stream(stream_id)

