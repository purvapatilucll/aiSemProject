from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_destinations(user, destinations_df):
    user_text = f"""
    The user is interested in {user['preferred_location_type']} places, uses {user['preferred_device']}, 
    has {user['member_in_family']} family members, and spends around {user['Daily_Avg_mins_spend_on_traveling_page']} mins daily on travel pages. 
    They like {user['total_likes_on_outstation_checkin_given']} travel posts and comment frequently ({user['Yearly_avg_comment_on_travel_page']}).
    """

    user_embedding = model.encode(user_text, convert_to_tensor=True)

    destinations_df["text_for_matching"] = destinations_df.apply(lambda row: f"{row['Destination']} {row['Region']} {row['Category']} {row['Description']} {row['Famous Foods']}", axis=1)

    destination_embeddings = model.encode(destinations_df["text_for_matching"].tolist(), convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(user_embedding, destination_embeddings)[0]

    destinations_df["similarity"] = similarities.cpu().numpy()

    top_matches = destinations_df.sort_values(by="similarity", ascending=False).head(3)

    return top_matches.to_dict(orient="records")
