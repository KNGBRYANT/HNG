import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from PIL import Image
Image.MAX_IMAGE_PIXELS = None

df = pd.read_csv("cleaned_movie_dataset.csv")
df['last_rating_date'] = pd.to_datetime(df['last_rating_date'], errors='coerce')
df['avg_rating'] = df['avg_rating'].round(1)

st.title("MovieLens Exploratory Analysis")
st.write("Explore and analyze movie ratings, genres, tags, and key features from the MovieLens dataset. This dashboard lets you uncover insights, identify trends, and interactively filter movies by genre, rating, year, etc. to support data-driven decisions and recommendations.")

# Filters
genre_filter = st.multiselect("Select Genre(s)", options=df['main_genre'].unique(), default=df['main_genre'].unique())
df_filtered = df[df['main_genre'].isin(genre_filter)]



st.subheader("Raw Movie Data")
st.write("View the raw dataset below. Use the slider to choose how many rows to display.")

# Slider to select number of rows
num_rows = st.slider("Number of rows to view:", min_value=5, max_value=100, value=10, step=5)

# Display the selected number of rows
st.dataframe(df.head(num_rows))


st.subheader("Top 10 Highest Rated Movies")
top10 = df_filtered.sort_values('avg_rating', ascending=False).head(10)[['title','release_year','avg_rating']]
top10['avg_rating'] = top10['avg_rating'].map("{:.1f}".format)
st.table(top10)

st.subheader("Top 10 Lowest Rated Movies")
lowest_rated = df_filtered.sort_values('avg_rating', ascending=True).head(10)
# Format avg_rating to 1 decimal as string
lowest_rated['avg_rating'] = lowest_rated['avg_rating'].map('{:.1f}'.format)
st.table(lowest_rated[['title', 'release_year', 'avg_rating']])



st.subheader("Average Rating by Number of Genres")

avg_rating_by_genres = df_filtered.groupby('num_genres')['avg_rating'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x='num_genres', 
    y='avg_rating', 
    data=avg_rating_by_genres, 
    palette="rocket", 
    edgecolor='black',
    ax=ax
)
for index, row in avg_rating_by_genres.iterrows():
    ax.text(row.name, row.avg_rating + 0.02, f"{row.avg_rating:.1f}", ha='center', va='bottom')

ax.set_xlabel("Number of Genres")
ax.set_ylabel("Average Rating")
ax.set_title("Average Rating by Number of Genres")
st.pyplot(fig)



st.subheader("Distribution of Average Ratings")
df_filtered['avg_rating_rounded'] = df_filtered['avg_rating'].round(1)

fig, ax = plt.subplots(figsize=(10,5))
sns.histplot(
    df_filtered['avg_rating_rounded'], 
    bins=20, 
    kde=True,           # add smooth density curve
    color='lightseagreen', 
    edgecolor='black', 
    ax=ax
)
mean_rating = df_filtered['avg_rating_rounded'].mean()
ax.axvline(mean_rating, color='red', linestyle='--', label=f"Mean Rating: {mean_rating:.1f}")
ax.set_xlabel("Average Rating")
ax.set_ylabel("Number of Movies")
ax.set_title("Distribution of Average Ratings with Density Curve")
ax.legend()
st.pyplot(fig)


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


st.subheader("Top 10 Most Tagged Movies")
df_known = df_filtered[df_filtered['title'] != 'Unknown']
most_tagged = df_known.sort_values('N0_of_tags', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y='title',
    x='N0_of_tags',
    data=most_tagged,
    palette='plasma',
    edgecolor='black',
    ax=ax
)
for index, row in most_tagged.iterrows():
    ax.text(row.N0_of_tags + 1, index, round(row.N0_of_tags, 1), va='center')
ax.set_xlabel("Number of Tags")
ax.set_ylabel("Movie Title")
ax.set_title("Top 10 Most Tagged Movies (Excluding Unknown)")
st.pyplot(fig)




st.subheader("Top 10 Most Tagged Movies")

most_tagged = df_filtered[df_filtered['title'].str.lower() != 'unknown']
most_tagged = most_tagged.sort_values('N0_of_tags', ascending=False).head(10)

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y='title',
    x='N0_of_tags',
    data=most_tagged,
    palette='plasma',
    edgecolor='black',
    ax=ax
)

for i, v in enumerate(most_tagged['N0_of_tags']):
    ax.text(v + 0.5, i, f"{int(v)}", va='center', fontweight='bold', fontsize=10, color='black')

ax.set_xlabel("Number of Tags", fontsize=12)
ax.set_ylabel("Movie Title", fontsize=12)
ax.set_title("Top 10 Most Tagged Movies", fontsize=14, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.6)
sns.despine(left=True, bottom=True)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)



st.subheader("Movie Age vs Average Rating")

fig, ax = plt.subplots(figsize=(12,6))
sns.scatterplot(
    data=df_filtered,
    x='movie_age', 
    y='avg_rating', 
    size='N0_of_tags',  # size indicates popularity
    hue='avg_rating',   # color by rating
    palette='cool', 
    sizes=(20,200),
    alpha=0.7,
    ax=ax
)
ax.set_xlabel("Movie Age (Years)")
ax.set_ylabel("Average Rating")
ax.set_title("Movie Age vs Average Rating (Size=Number of Tags)")
st.pyplot(fig)


