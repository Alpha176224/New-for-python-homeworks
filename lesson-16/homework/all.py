import pandas as pd
import sqlite3

# Part 1
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))

iris_df = pd.read_json("iris.json")
print(iris_df.shape)
print(iris_df.columns)

titanic_df = pd.read_excel("titanic.xlsx")
print(titanic_df.head())

flights_df = pd.read_parquet("flights.parquet")
print(flights_df.info())

movie_df = pd.read_csv("movie.csv")
print(movie_df.sample(10))

# Part 2
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[["sepal_length", "sepal_width"]]
print(iris_selected.head())

titanic_filtered = titanic_df[titanic_df["Age"] > 30]
print(titanic_filtered)

gender_counts = titanic_df["Sex"].value_counts()
print(gender_counts)

flights_selected = flights_df[["origin", "dest", "carrier"]]
print(flights_selected.head())

unique_destinations = flights_df["dest"].nunique()
print(unique_destinations)

movie_filtered = movie_df[movie_df["duration"] > 120]
movie_sorted = movie_filtered.sort_values("director_facebook_likes", ascending=False)
print(movie_sorted.head())

# Part 3
iris_stats = iris_df.describe().loc[["mean", "50%", "std"]]
print(iris_stats)

titanic_ages = titanic_df["Age"]
print(titanic_ages.min(), titanic_ages.max(), titanic_ages.sum())

director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print(director_likes)

longest_movies = movie_df.sort_values("duration", ascending=False)[["duration", "director_name"]].head(5)
print(longest_movies)

missing_values = flights_df.isnull().sum()
print(missing_values)

num_cols = flights_df.select_dtypes(include="number").columns
for col in num_cols:
    flights_df[col] = flights_df[col].fillna(flights_df[col].mean())
