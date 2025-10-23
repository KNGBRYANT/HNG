import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

# Prevent image size warning
Image.MAX_IMAGE_PIXELS = None

# ==============================
# Load Data
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_movie_dataset.csv")
    df['last_rating_date'] = pd.to_datetime(df['last_rating_date'], errors='coerce')
    df['avg_rating'] = df['avg_rating'].round(1)
    return df

df = load_data()
df.columns = [col.replace("_", " ").title() for col in df.columns]

# ==============================
# Title and Introduction
# ==============================
st.title("🎬 MovieLens Exploratory Dashboard")
st.markdown("""
Welcome to the **interactive MovieLens dashboard**.  
Explore and analyze ratings, genres, tags, and trends.  
Use filters to focus on what matters most!
""")

# ==============================
# Filters
# ==============================
genre_filter = st.multiselect(
    "🎭 Select Genre(s):",
    options=df['main_genre'].dropna().unique().tolist(),
    default=df['main_genre'].dropna().unique().tolist()
)

df_filtered = df[df['main_genre'].isin(genre_filter)]

# ==============================
# Raw Data Section
# ==============================
st.header("📊 Raw Movie Data")

num_rows = st.slider("Number of rows to view:", 5, 100, 10, step=5)
st.dataframe(df.head(num_rows))

# ---- Section: Ratings Overview ----
st.markdown("🎬 Movie Ratings Overview")

# Format column names to look professional (e.g., 'Release Year' instead of 'release_year')
df.columns = [col.replace("_", " ").title() for col in df.columns]

# Top 10 Highest Rated Movies
st.markdown("⭐ Top 10 Highest Rated Movies")
top_highest = df.sort_values("Imdb Rating", ascending=False).head(10)
st.dataframe(
    top_highest.style.hide(axis="index"),
    use_container_width=True
)

st.markdown("---")  # horizontal line for separation

# Top 10 Lowest Rated Movies
st.markdown("💔 Top 10 Lowest Rated Movies")
top_lowest = df.sort_values("Imdb Rating", ascending=True).head(10)
st.dataframe(
    top_lowest.style.hide(axis="index"),
    use_container_width=True
)


# ==============================
# Average Rating by Number of Genres
# ==============================
st.header("🎭 Average Rating by Number of Genres")

avg_rating_by_genres = df_filtered.groupby('num_genres')['avg_rating'].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(
    x='num_genres', y='avg_rating',
    data=avg_rating_by_genres, palette='rocket', ax=ax
)
ax.set_xlabel("Number of Genres")
ax.set_ylabel("Average Rating")
ax.set_title("Average Rating vs Number of Genres", fontsize=12)
st.pyplot(fig)
plt.close(fig)

# ==============================
# Distribution of Average Ratings
# ==============================
st.header("🎨 Distribution of Average Ratings")

fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(df_filtered['avg_rating'], bins=20, kde=True, color='teal', edgecolor='black', ax=ax)
mean_rating = df_filtered['avg_rating'].mean()
ax.axvline(mean_rating, color='red', linestyle='--', label=f"Mean: {mean_rating:.1f}")
ax.legend()
st.pyplot(fig)
plt.close(fig)

# ==============================
# Top 10 Most Tagged Movies
# ==============================
st.header("🏷️ Top 10 Most Tagged Movies")

df_known = df_filtered[df_filtered['title'].str.lower() != 'unknown']
most_tagged = df_known.sort_values('N0_of_tags', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y='title', x='N0_of_tags',
    data=most_tagged, palette='plasma', ax=ax
)
for i, v in enumerate(most_tagged['N0_of_tags']):
    ax.text(v + 0.3, i, f"{int(v)}", va='center', fontsize=9)
ax.set_xlabel("Number of Tags")
ax.set_ylabel("Movie Title")
ax.set_title("Top 10 Most Tagged Movies (Excluding Unknown)")
st.pyplot(fig)
plt.close(fig)
