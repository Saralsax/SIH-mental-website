import csv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List

# Initialize the FastAPI application
app = FastAPI(
    title="Counselor Booking API",
    description="API for finding and booking mental wellness counselors.",
    version="1.1.0",
)

# --- Add CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models for Request Validation ---
class FindCounselorRequest(BaseModel):
    specialty: str

class BookingRequest(BaseModel):
    user_id: int
    counselor_id: int
    slot_id: int

# --- Database (Loaded from CSV) ---
COUNSELORS = {}
USERS = {
    101: {"id": 101, "name": "Alice"},
    102: {"id": 102, "name": "Bob"}
}
BOOKINGS = []
booking_id_counter = 1

def load_counselors_from_csv(file_path: str):
    """Reads counselor data from a CSV and populates the in-memory database."""
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                counselor_id = int(row["id"])
                
                # Generate some default availability for demonstration
                availability = []
                base_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
                for i in range(3):
                    availability.append({
                        "slot_id": (counselor_id * 100) + i,
                        "start_time": base_time + timedelta(hours=i),
                        "status": "available"
                    })

                COUNSELORS[counselor_id] = {
                    "id": counselor_id,
                    "name": row["name"],
                    "specialties": [s.strip() for s in row["specialties"].split(',')[1:]],
                    "availability": availability
                }
        print(f"Successfully loaded {len(COUNSELORS)} counselors from {file_path}")
    except FileNotFoundError:
        print(f"ERROR: Counselor CSV file not found at {file_path}. Please create it.")
    except Exception as e:
        print(f"An error occurred while loading counselors: {e}")

# --- Helper Functions ---
def format_counselor_for_response(counselor):
    """Formats counselor data, converting datetime to string for JSON compatibility."""
    counselor_data = {k: v for k, v in counselor.items() if k != 'availability'}
    counselor_data['availability'] = [
        {
            "slot_id": slot["slot_id"],
            "start_time": slot["start_time"].isoformat(),
            "status": slot["status"]
        } for slot in counselor.get('availability', [])
    ]
    return counselor_data

# --- API Endpoints ---
@app.post("/api/find-counselor")
async def find_counselor(request: FindCounselorRequest):
    """
    Finds all available counselors for a specific specialty.
    """
    required_specialty = request.specialty
    
    # Find all counselors who list the required specialty
    matching_counselors = [
        c for c in COUNSELORS.values() if required_specialty in c['specialties']
    ]

    # Filter down to only those who have at least one available slot in the future
    available_counselors = []
    for counselor in matching_counselors:
        has_available_slot = any(
            slot['status'] == 'available' and slot['start_time'] > datetime.now()
            for slot in counselor['availability']
        )
        if has_available_slot:
            available_counselors.append(format_counselor_for_response(counselor))

    if not available_counselors:
        raise HTTPException(
            status_code=404, 
            detail=f"No available counselors found for specialty: {required_specialty}"
        )

    return {
        "message": f"Found {len(available_counselors)} available counselors.",
        "counselors": available_counselors
    }

# ... (The rest of the endpoints: /api/book, /api/counselors, etc. remain the same)
@app.post("/api/book", status_code=201)
async def book_consultation(request: BookingRequest):
    """
    Books a consultation slot with a specific counselor for a user.
    """
    global booking_id_counter
    user_id = request.user_id
    counselor_id = request.counselor_id
    slot_id = request.slot_id

    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found.")
    if counselor_id not in COUNSELORS:
        raise HTTPException(status_code=404, detail="Counselor not found.")

    counselor = COUNSELORS[counselor_id]
    
    target_slot = next((slot for slot in counselor['availability'] if slot['slot_id'] == slot_id), None)
            
    if not target_slot:
        raise HTTPException(status_code=404, detail="Time slot not found.")

    if target_slot['status'] != 'available':
        raise HTTPException(status_code=409, detail="This time slot is already booked.")

    target_slot['status'] = 'booked'

    new_booking = {
        "booking_id": booking_id_counter,
        "user_id": user_id,
        "counselor_id": counselor_id,
        "counselor_name": counselor['name'],
        "start_time": target_slot['start_time'].isoformat(),
        "status": "confirmed"
    }
    BOOKINGS.append(new_booking)
    booking_id_counter += 1

    return {
        "message": "Booking confirmed!",
        "booking_details": new_booking
    }

@app.get("/api/counselors")
async def get_counselors():
    """Returns a list of all counselors and their details."""
    return [format_counselor_for_response(c) for c in COUNSELORS.values()]

@app.get("/api/user/{user_id}/bookings")
async def get_user_bookings(user_id: int):
    """Returns all bookings for a specific user."""
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found.")
        
    user_bookings = [b for b in BOOKINGS if b['user_id'] == user_id]
    
    if not user_bookings:
        return {"message": "No bookings found for this user."}
        
    return user_bookings


# --- Server Startup ---
# Load the counselor data when the application starts
load_counselors_from_csv('counselors.csv')

