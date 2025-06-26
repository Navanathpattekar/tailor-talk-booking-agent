
def get_availability(request):
    return {"available_slots": ["2025-06-26T15:00:00", "2025-06-26T16:00:00"]}

def book_slot(request):
    return {"status": "confirmed", "slot": request.time}
