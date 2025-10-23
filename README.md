# 🎬 MovieLens Feature Engineering & EDA Dashboard

A comprehensive **Feature Engineering** and **Exploratory Data Analysis (EDA)** project built using the **MovieLens dataset**.  
This interactive dashboard, deployed via [Streamlit](https://movie-dashboard1.streamlit.app/), provides data-driven insights into movie characteristics, audience ratings, tagging behavior, and patterns that can power intelligent **movie recommendation systems**.

---

## 🌐 Live App

🚀 **Try it here:** [https://movie-dashboard1.streamlit.app/](https://movie-dashboard1.streamlit.app/)

---

## 📘 Project Overview

This project explores and visualizes the **MovieLens dataset** to uncover insights about how movies are rated, tagged, and perceived over time.  
It combines **feature engineering**, **data cleaning**, and **visual storytelling** in Streamlit to help users interact with the data and understand key trends.

The main objectives were to:

- Engineer meaningful features that enrich the raw dataset.
- Perform detailed exploratory data analysis (EDA) to uncover rating patterns.
- Build an interactive Streamlit dashboard for visualization.
- Generate insights that can inform the development of **recommendation systems**.

---

## 📂 Repository Contents

| File/Folder | Description |
|--------------|-------------|
| `Engineer.ipynb` | Jupyter Notebook containing full analysis and feature engineering steps. |
| `Engineer.py` | Streamlit dashboard script. |
| `requirements.txt` | Dependencies needed to run the dashboard locally. |
| `cleaned_movie_data.csv` | Processed and feature-enhanced dataset used for visualization. |
| `MovieLens_Report.pdf` | Full written report (Stage 1 — Feature Engineering & EDA). |
| `README.md` | This documentation file. |

---

## 🧠 Features Engineered

| Feature | Description | Purpose |
|----------|--------------|----------|
| `release_year` | Extracted from movie title. | Analyzes rating trends over time. |
| `movie_age` | Current year minus release year. | Studies how age affects popularity and rating. |
| `num_genres` | Count of genres assigned to a movie. | Explores diversity and audience appeal. |
| `main_genre` | Primary genre extracted from the list. | Enables genre-based grouping and comparisons. |
| `N0_of_tags` | Number of tags per movie. | Measures engagement and popularity. |
| `rating_year` | Year of the most recent rating. | Analyzes temporal changes in viewer activity. |
| `avg_rating` | Average rating per movie. | Core metric for evaluating audience satisfaction. |
| `tag` | Combined tag strings. | Allows text-based exploration of themes. |

---

## 📊 Exploratory Data Analysis (EDA)

The dashboard is organized into multiple sections, each exploring different aspects of the dataset.

### 1️⃣ **Distribution of Average Ratings**
- Displays the overall spread of movie ratings.
- Most movies fall between **3–4 stars**, indicating balanced viewer sentiment.

🖼 **Screenshot Suggestion:**  
Take a screenshot of the "Distribution of Average Ratings" bar chart.

---

### 2️⃣ **Average Rating by Number of Genres**
- Movies with **3–4 genres** tend to receive slightly higher ratings (~3.3–3.4).
- Overly diverse genre combinations (8–10) don’t show major improvements.

🖼 **Screenshot Suggestion:**  
Capture the bar plot comparing number of genres vs. average ratings.

---

### 3️⃣ **Genre vs Rating vs Age**
- Older **Documentary** and **Animation** movies perform best (~3.5 avg rating).
- **Horror** consistently scores lower (~2.8).

🖼 **Screenshot Suggestion:**  
Show the grouped bar or bubble chart with genre vs age vs rating.

---

### 4️⃣ **Movie Age vs Average Rating**
- Newer movies dominate rating activity.
- Older classics (40–60 years) maintain strong, stable ratings.

🖼 **Screenshot Suggestion:**  
Include scatter plot visualization with age vs. rating (bubble size = tags).

---

### 5️⃣ **Top 10 Highest & Lowest Rated Movies**
- Lists the most loved and least liked movies by audience score.

🖼 **Screenshot Suggestion:**  
Take two separate screenshots showing:
1. “⭐ Top 10 Highest Rated Movies” table  
2. “💔 Top 10 Lowest Rated Movies” table  

---

### 6️⃣ **Top 10 Most Tagged Movies**
- **Pulp Fiction**, **Fight Club**, and **2001: A Space Odyssey** lead engagement.
- High tagging reflects community interest and discussion value.

🖼 **Screenshot Suggestion:**  
Include screenshot of bar chart showing the most tagged movies.

---

### 7️⃣ **Top 10 Most Common Tags**
- Frequent tags: “In Netflix Queue”, “Atmospheric”, “Superhero”.
- Indicates ongoing viewer themes and streaming relevance.

🖼 **Screenshot Suggestion:**  
Capture the tag frequency visualization.

---

## 💡 Key Insights

| Theme | Observation | Relevance |
|--------|--------------|------------|
| 🎭 **Genres & Tags** | Users tag movies more when emotionally connected. | Helps identify clusters for recommendations. |
| ⭐ **Ratings Stability** | Ratings cluster around 3–4 stars. | Indicates balanced user sentiment. |
| 🎞 **Movie Age** | Older movies still maintain strong ratings. | Useful for mixing new + classic recommendations. |
| 🧩 **Genre Importance** | Documentary and Animation films perform better. | Supports genre-based recommendation weighting. |

---

## 🧩 Recommendation System Implications

This analysis provides the groundwork for **content-based** and **collaborative filtering** methods:

- `main_genre` and `num_genres` → Cluster movies by similarity.  
- `avg_rating` and `movie_age` → Balance trending vs. classic recommendations.  
- `N0_of_tags` → Weight movies by community engagement.  
- `tag` → Enhance similarity detection via tag-based themes.

---

## 🧰 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/MovieLens-EDA-Dashboard.git
cd MovieLens-EDA-Dashboard
