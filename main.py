from recommender import recommend_destinations
from llm_generator import generate_itinerary
import pandas as pd


users = pd.read_csv("data/users.csv", encoding='latin1')
destinations = pd.read_csv("data/destinations.csv", encoding='latin1')  

user_id = 1000001
user_profile = users[users["UserID"] == user_id].iloc[0]


recommended = recommend_destinations(user_profile, destinations)

for i, dest in enumerate(recommended):
    dest["Day"] = (i % 3) + 1

itinerary = generate_itinerary(user_profile, recommended)

print(itinerary)
