import streamlit as st
import pandas as pd
from recommender import recommend_destinations
from llm_generator import *
import requests
import os
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_API_URL = os.getenv("PEXELS_API_URL")

users = pd.read_csv("data/users.csv")
destinations = pd.read_csv("data/destinations.csv", encoding='latin1')

st.set_page_config(page_title="AI Travel Itinerary Recommender", layout="centered")

st.title("✈️ AI Travel Itinerary Recommender")

user_ids = users["UserID"].tolist()
selected_user_id = st.selectbox("Choose a User ID", user_ids)

user_profile = users[users["UserID"] == selected_user_id].iloc[0]

with st.expander("🔍 View Selected User Profile"):
    st.json(user_profile.to_dict())

recommended = recommend_destinations(user_profile, destinations)


def fetch_pexels_image(query):
    headers = {
        'Authorization': PEXELS_API_KEY
    }
    params = {
        'query': query,
        'per_page': 1
    }
    response = requests.get(PEXELS_API_URL, headers=headers, params=params)
    data = response.json()

    if data['photos']:
        return data['photos'][0]['src']['medium']
    else:
        return None

st.subheader("🏝️ Recommended Destinations")
for dest in recommended:
    image_url = fetch_pexels_image(dest['Destination'])
    if image_url:
        st.image(image_url, caption=dest['Destination'], use_container_width=True)
    st.markdown(f"### {dest['Destination']} ({dest['Region']}, {dest['Country']})")
    st.markdown(f"- **Famous Foods:** {dest['Famous Foods']}")
    st.markdown(f"- **Best Time to Visit:** {dest['Best Time to Visit']}")
    st.markdown(f"- **Safety:** {dest['Safety']}")
    st.markdown(f"- **Why go:** {dest['Description']}")
    st.markdown("---")


st.subheader("🚉 Choose Your Travel Mode")
travel_mode = st.radio(
    "How do you plan to travel?",
    ("Car", "Public Transport")
)


if st.button("🧳 Generate My Travel Itinerary"):
    with st.spinner("Generating itinerary with AI..."):
        itinerary = generate_itinerary(user_profile, recommended, travel_mode)
        st.subheader("📝 Your Personalized Itinerary")
        st.markdown(itinerary)