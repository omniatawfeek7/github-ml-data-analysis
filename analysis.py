import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("github_projects.csv")

print("Cleaned dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Basic statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())
# Correlation analysis
correlation_columns = [
    "stargazers_count",
    "forks_count",
    "open_issues_count",
    "repository_age_years",
    "days_since_update"
]
print("\nCorrelation matrix:")
print(df[correlation_columns].corr().round(2))
import matplotlib.pyplot as plt

# Stars vs Forks
plt.figure(figsize=(8, 5))
plt.scatter(df["stargazers_count"], df["forks_count"], alpha=0.7)

plt.xlabel("Stars")
plt.ylabel("Forks")
plt.title("Stars vs Forks of Machine Learning Repositories")

plt.tight_layout()
plt.show()
# Stars vs Days Since Update
plt.figure(figsize=(8, 5))
plt.scatter(df["days_since_update"], df["stargazers_count"], alpha=0.7)

plt.xlabel("Days Since Last Update")
plt.ylabel("Stars")
plt.title("Repository Activity vs Stars")

plt.tight_layout()
plt.show()
# Most common programming languages

language_counts = df["language"].value_counts()

print("\nMost common programming languages:")
print(language_counts.head(10))
# Average stars by programming language

language_stars = (
    df.groupby("language")["stargazers_count"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage stars by programming language:")
print(language_stars)
# Number of repositories for each language

language_counts = df["language"].value_counts()

print("\nLanguages with at least 3 repositories:")
print(language_counts[language_counts >= 3])
# Most common languages chart

common_languages = language_counts[language_counts >= 3]

plt.figure(figsize=(8, 5))
common_languages.plot(kind="bar")

plt.xlabel("Language")
plt.ylabel("Number of Repositories")
plt.title("Most Common Languages in the Dataset")

plt.tight_layout()
plt.show()