
from fastapi import FastAPI
from app.calendar_utils import get_availability, book_slot
from app.schemas import BookingRequest

app = FastAPI()

@app.post("/check_availability/")
async def check_availability(request: BookingRequest):
    return get_availability(request)

@app.post("/book_slot/")
async def book_slot_endpoint(request: BookingRequest):
    return book_slot(request)
