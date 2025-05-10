# AI Travel Itinerary Recommender


**AI Travel Itinerary Recommender** is web application that recommends personalized travel destinations and generates detailed 3-day itineraries based on:
- User interests
- Family size
- Travel habits
- Preferred transport mode (Car / Public Transport)

It uses **Sentence Transformers** for semantic recommendation, **LLMs (Large Language Models)** for personalized itinerary generation, and **Streamlit** for building an interactive front-end.


## Prerequisites & Dependencies

### Required Python Packages

1. **streamlit**: Web framework for building the interactive user interface.
2. **pandas**: For managing data, such as user profiles and destination information.
3. **requests**: For making HTTP requests to external APIs (like Pexels API to fetch destination images).
5. **sentence-transformers**: For generating sentence embeddings and calculating semantic similarity between user profiles and destinations.
6. **openai**: To connect to OpenAI's GPT model for itinerary generation.

---

## Github Repository

https://github.com/purvapatilucll/aiSemProject

```
# Clone the repository
git clone https://github.com/purvapatilucll/aiSemProject.git

# Navigate into the project directory
cd aiSemProject

# Run the Streamlit app
streamlit run app.py
```



## Dataset Information

### 1. Destinations Dataset (`destinations.csv`)
This dataset contains major tourist destinations with detailed metadata.

| Column                  | Description |
|--------------------------|-------------|
| Destination              | Name of the place (e.g., Rome) |
| Region                   | Region name (e.g., Lazio) |
| Country                  | Country (e.g., Italy) |
| Category                 | City / Coastal Town / Lake |
| Latitude, Longitude      | Geo-coordinates |
| Approximate Annual Tourists | Number of approx visitors yearly |
| Currency                 | Currency used |
| Majority Religion        | Major religion |
| Famous Foods             | Local cuisine |
| Language                 | Primary language |
| Best Time to Visit       | Seasonal recommendation |
| Cost of Living           | General cost of living |
| Safety                   | Safety level |
| Cultural Significance    | Heritage/cultural value |
| Description              | Brief overview of the destination |



### 2. Users Dataset (`users.csv`)
This dataset represents user profiles with behavioral and demographic traits.

| Column                         | Description |
|---------------------------------|-------------|
| UserID                          | Unique user ID |
| Taken_product                   | Whether user has purchased travel-related products |
| Yearly_avg_view_on_travel_page  | Average yearly views on travl pages (indicated level of travel interest) |
| preferred_device                | Device used by the user |
| total_likes_on_outstation_checkin_given | Engagement on travel content |
| yearly_avg_Outstation_checkins  | Frequency of travel |
| member_in_family                | Family size |
| preferred_location_type         | Financial / Medical / Other (needs for travel) |
| Yearly_avg_comment_on_travel_page | Average Comments on travel posts |
| total_likes_on_outofstation_checkin_received | Total likes received on out of station checkin |
| week_since_last_outstation_checkin | Recent travel |
| following_company_page          | Following company page on social media |
| montly_avg_comment_on_company_page | Monthly average comment on company page |
| working_flag                    | Working status |
| travelling_network_rating       | Rating of travelling network |
| Adult_flag                      | Whether adult |
| Daily_Avg_mins_spend_on_traveling_page | Daily average minutes spend on the travel page  |

---

## Core Modules

### 1. recommender.py
- **Model**: Uses [`sentence-transformers` -> `all-MiniLM-L6-v2`] to embed user profile text and destination descriptions.
- **Similarity Calculation**: Measures similarity between the user's embedding and destination embeddings.
- **Top Matches**: Returns the top 3 most semantically similar destinations.

### 2. llm_generator.py

- **Model API**: Uses Together.xyz's OpenAI-compatible API (`mistralai/Mistral-7B-Instruct-v0.1`).
- **Feature**: considers **user's preferred travel mode** (`Car` or `Public Transport`).
- **Transport-based Logic**:
  - If `Car`, suggests scenic drives, parking spots, and self-driving exploration.
  - If `Public Transport`, suggests airports, bus/train stations, local public transport options.
- **Itinerary Details**:
  - Morning, afternoon, evening activities
  - Local food recommendations
  - Clothing and safety tips
  - Light optional activities for flexible travelers

### 3. app.py

- **Framework**: Streamlit
- **User Interface**:
  - User ID selection (`selectbox`)
  - User profile preview (`st.expander`)
  - Destination recommendation (with **real images** from Pexels API (NOTE: pictures doesn't fully work as expected))
  - Radio button (`st.radio`) for selecting Travel Mode (Car / Public Transport)
- **Itinerary Generation**:
  - Button ("Generate My Travel Itinerary") triggers LLM with travel mode passed as parameter.



## APIs and Libraries

| Tool/Library | Purpose |
|--------------|---------|
| sentence-transformers | Embedding and semantic similarity |
| Together.xyz API (Mistral-7B) | LLM itinerary generation |
| Streamlit | Frontend web app |
| Pexels API | Fetch travel images |



## Key Workflow

1. **User selects their ID**
2. **Top 3 matching destinations** are recommended
3. **Real images** shown for each destination (it is not that efficient)
4. **User selects travel mode** (Car/Public Transport)
5. **Itinerary generated** with transport-specific advice and personalized trip plans.


