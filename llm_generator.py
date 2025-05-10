from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


TogetherAI_API_KEY = os.getenv("TogetherAI_API_KEY")
TogetherAI_BASE_URL = os.getenv("TogetherAI_BASE_URL")

client = OpenAI(
    api_key=TogetherAI_API_KEY,
    base_url=TogetherAI_BASE_URL
)

def generate_itinerary(user_profile, destinations, transport_mode):
    prompt = f"""You are a travel assistant. The user has this profile:
- Likes {user_profile['preferred_location_type']} locations
- Family Members: {user_profile['member_in_family']}
- Likes: {user_profile['total_likes_on_outstation_checkin_given']}
- Preferred Mode of Transport: {transport_mode}

Based on this, generate a personalized, detailed 3-day itinerary **for each destination separately**.

**Important**:
- If the user is using **Private Car**, assume they will **drive to the destination** and **explore using their own car**. Avoid suggesting airport arrivals. Instead, suggest parking spots, drive routes, scenic drives, etc.
- If using **Public Transport**, you can suggest arriving at airports, bus stations, or train stations, and mention local bus/train routes.

For each destination:
- Day 1: Arrival activities, light exploration
- Day 2: Full day activities (hikes, museums, sightseeing, etc.)
- Day 3: Relaxation, shopping, local experiences, and departure

Here are the destinations:

{format_destinations(destinations)}

Make the tone friendly, but detailed and realistic. Include:
- Morning, afternoon, evening plans for each day
- Local food to try
- Travel tips (clothing, transportation, safety)
- Light optional suggestions (in case the traveler is tired)
"""

    try:
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"

def format_destinations(dest_list):
    return "\n".join([
        f"{d['Destination']} ({d['Region']}, {d['Country']}): {d['Description']}" for d in dest_list
    ])

def ask_transport_mode():
    print("Select your preferred mode of transport:")
    print("1. Public Transport (Bus, Train)")
    print("2. Rental Car")
    print("3. Taxi or Rideshare (Uber, Lyft)")
    choice = input("Enter the number corresponding to your choice: ")

    transport_options = {
        "1": "Public Transport",
        "2": "Rental Car",
        "3": "Taxi or Rideshare"
    }
    return transport_options.get(choice, "Public Transport")  # Default to Public if invalid input
