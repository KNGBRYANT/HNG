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
- Most movies fall between **2.5–4.2 stars**, indicating balanced viewer sentiment.

![Distribution of Average Ratings](Images/Distribution%20of%20Average%20Ratings.png)

---

### 2️⃣ **Average Rating by Number of Genres**
- Movies with **7 genres** tend to receive slightly higher ratings (~3.3–3.4).
- Overly diverse genre combinations (10) show higher improvements.

![Average Ratings by Number Of Genres](Images/Average%20Ratings%20by%20Number%20Of%20Genres.png)

---

### 3️⃣ **Genre vs Rating vs Age**
- Older **Documentary** and **Animation** movies perform best (~3.5 avg rating).
- **Horror** consistently scores lower (~2.8).

![Genre VS Ratings VS Age](Images/Genre%20VS%20Ratings%20VS%20Age.png)

---

### 4️⃣ **Movie Age vs Average Rating**
- Newer movies are fewer compared to older ones.
- Their ratings mostly cluster between 2.5 and 4.

![Movie Age VS Ratings](Images/Movie%20Age%20VS%20Ratings.png)

---

### 5️⃣ **Top 10 Highest & Lowest Rated Movies**
- Lists the most loved and least liked movies by audience score.

![Highest Rated Movie](Images/Screenshot%202025-10-23%20175541.png)

![Lowest Rated Movie](Images/Screenshot%202025-10-23%20175558.png)

---

### 6️⃣ **Top 10 Most Tagged Movies**
- **Pulp Fiction**, **Fight Club**, and **2001: A Space Odyssey** lead engagement.
- High tagging reflects community interest and discussion value.

![Top 10 Most Tagged Movies](Images/Top%2010%20Most%20Tag%20Movies.png)

---

### 7️⃣ **Top 10 Most Common Tags**
- Frequent tags: “In Netflix Queue”, “Atmospheric”, “Superhero”.
- Indicates ongoing viewer themes and streaming relevance.

![Top 10 Most Common Movie Tags](Images/Top%2010%20Most%20common%20movie%20tag.png)

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

## 🎨 Dashboard Filters
The dashboard includes interactive filters that allow you to:

- Select movie age ranges (every 10 years)
- Choose rating ranges (0.0–5.0)
- View filtered results across all charts and tables in real-time

**🖼 Screenshot Suggestion:**  
Show the sidebar filter panel.

---

## 📄 Dataset Summary

**Summary**

This dataset (`ml-latest-small`) describes 5-star rating and free-text tagging activity from **MovieLens**, a movie recommendation service.  
It contains **100,836 ratings** and **3,683 tag applications** across **9,742 movies**, generated by **610 users** between **March 29, 1996** and **September 24, 2018**.

Users were selected randomly, each having rated at least 20 movies.  
No demographic data is included.  
Dataset generated on **September 26, 2018**.

**Files Included**
- `ratings.csv` — Ratings data (`userId`, `movieId`, `rating`, `timestamp`)
- `tags.csv` — User-applied tags for each movie
- `movies.csv` — Movie titles and genres
- `links.csv` — Links to IMDB and TMDB IDs

**📚 Full Dataset and Documentation:**  
[MovieLens Datasets — GroupLens](http://grouplens.org/datasets/movielens/)

---

## ⚖️ Usage License

This dataset is made available by the **GroupLens Research Group (University of Minnesota)** under the following conditions:

- The dataset may be used for research purposes only.  
- Redistribution is allowed under the same license conditions.  
- No endorsement by the University of Minnesota should be implied.  
- Commercial use requires prior permission.

> “The data set may be used for any research purposes under the conditions listed above.  
> The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission.”

For inquiries, contact: **grouplens-info@umn.edu**

---

## 🧾 Citation

If you use this dataset, please cite:

> F. Maxwell Harper and Joseph A. Konstan. 2015.  
> *The MovieLens Datasets: History and Context.*  
> ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19.  
> [https://doi.org/10.1145/2827872](https://doi.org/10.1145/2827872)

---

## 👩‍💻 Author

**Lawal Mayowa**  
*Stage 1 Submission — Feature Engineering & EDA*  
📧 Contact: [Lawal Mayowa](https://www.linkedin.com/in/lawal-mayowa-160bb930b/)

🌐 Live Dashboard: [https://movie-dashboard1.streamlit.app/](https://movie-dashboard1.streamlit.app/)

---

## 🏁 Conclusion

This project demonstrates how feature engineering and EDA can transform raw MovieLens data into actionable insights for future recommendation models.

### Key Takeaways
- Moderate genre diversity enhances ratings  
- Older movies retain long-term appreciation  
- Popular tags reveal audience-driven trends  
- High engagement correlates with strong community presence

The insights gained here form the foundation for building **intelligent movie recommendation systems** powered by user behavior, content similarity, and engagement metrics.

---

## 🪪 Acknowledgments

Special thanks to:
- **GroupLens Research, University of Minnesota** — for the open MovieLens datasets  
- **Streamlit** — for enabling beautiful interactive data apps  
- **Matplotlib, Seaborn, Pandas, and NumPy** — for analytics and visualization frameworks

