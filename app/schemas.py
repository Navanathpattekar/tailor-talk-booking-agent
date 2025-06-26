
from pydantic import BaseModel

class BookingRequest(BaseModel):
    user_name: str
    time: str
