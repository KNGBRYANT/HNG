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
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


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
# 🔍 Global Filters
# ==============================

st.sidebar.header("🎚️ Dashboard Filters")

# --- Genre Filter ---
genre_filter = st.sidebar.multiselect(
    "🎭 Select Genre(s):",
    options=df['main_genre'].dropna().unique().tolist(),
    default=df['main_genre'].dropna().unique().tolist()
)

# --- Movie Age Range Filter (every 10 years) ---
min_age = int(df['movie_age'].min())
max_age = int(df['movie_age'].max())

age_range = st.sidebar.slider(
    "🕰️ Select Movie Age Range (Years):",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age),
    step=10
)

# --- Rating Range Filter (0 to 5) ---
rating_range = st.sidebar.slider(
    "⭐ Select Average Rating Range:",
    min_value=0.0,
    max_value=5.0,
    value=(0.0, 5.0),
    step=0.5
)

# --- Apply Filters ---
df_filtered = df[
    (df['main_genre'].isin(genre_filter)) &
    (df['movie_age'].between(age_range[0], age_range[1])) &
    (df['avg_rating'].between(rating_range[0], rating_range[1]))
]

# ==============================
# Raw Data Section
# ==============================
st.header("📊 Raw Movie Data")

num_rows = st.slider("Number of rows to view:", 5, 100, 10, step=5)
st.dataframe(df.head(num_rows))

# ---- Section: Ratings Overview ----
st.markdown("🎬 Movie Ratings Overview")




# --- Top 10 Highest and Lowest Rated Movies ---
st.header("🎬 Movie Ratings Overview")

# Ensure column names are clean and consistent
df.columns = df.columns.str.strip().str.lower()

# --- Highest Rated Movies ---
st.subheader("⭐ Top 10 Highest Rated Movies")
top_highest = (
    df.sort_values("avg_rating", ascending=False)
      .head(10)[["title", "release_year", "avg_rating"]]
      .copy()
)
top_highest["avg_rating"] = top_highest["avg_rating"].map("{:.1f}".format)
top_highest.columns = ["Title", "Release Year", "Average Rating"]
st.table(top_highest)

# Add spacing between tables
st.markdown("---")

# --- Lowest Rated Movies ---
st.subheader("💔 Top 10 Lowest Rated Movies")
low_highest = (
    df.sort_values("avg_rating", ascending=True)
      .head(10)[["title", "release_year", "avg_rating"]]
      .copy()
)
low_highest["avg_rating"] = low_highest["avg_rating"].map("{:.1f}".format)
low_highest.columns = ["Title", "Release Year", "Average Rating"]
st.table(low_highest)



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
most_tagged = df_known.sort_values('n0_of_tags', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y='title', x='n0_of_tags',
    data=most_tagged, palette='plasma', ax=ax
)
for i, v in enumerate(most_tagged['n0_of_tags']):
    ax.text(v + 0.3, i, f"{int(v)}", va='center', fontsize=9)
ax.set_xlabel("Number of Tags")
ax.set_ylabel("Movie Title")
ax.set_title("Top 10 Most Tagged Movies (Excluding Unknown)")
st.pyplot(fig)
plt.close(fig)




st.subheader("Genre vs Rating vs Age")

fig, ax = plt.subplots(figsize=(12,6))
sns.scatterplot(
    data=df_filtered,
    x='movie_age', 
    y='avg_rating', 
    hue='main_genre', 
    palette='tab20', 
    s=100,  # marker size
    ax=ax
)
ax.set_xlabel("Movie Age (Years)")
ax.set_ylabel("Average Rating")
ax.set_title("Genre vs Rating vs Movie Age")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)



st.subheader("🎞️ Movie Age vs Average Rating")

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df_filtered,
    x='movie_age', 
    y='avg_rating', 
    size='n0_of_tags',   # ✅ lowercase column name
    hue='avg_rating',    # color by rating
    palette='viridis',   # smoother gradient color
    sizes=(30, 300),     # slightly larger bubbles
    alpha=0.7,
    ax=ax
)

# Add a subtle background grid
ax.grid(True, linestyle='--', alpha=0.3)

# Improve labels and title
ax.set_xlabel("🎬 Movie Age (Years)", fontsize=11)
ax.set_ylabel("⭐ Average Rating", fontsize=11)
ax.set_title("Movie Age vs Average Rating\n(Bubble Size = Number of Tags)", fontsize=14, fontweight='bold')

# Move the legend to the right for better clarity
ax.legend(title="Average Rating", bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the chart
st.pyplot(fig)
plt.close(fig)
