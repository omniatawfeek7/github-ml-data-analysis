import pandas as pd

# Load the raw dataset
df = pd.read_csv("github_raw.csv")

print("Raw dataset loaded successfully!")
print("Original shape:", df.shape)

# Select the columns required for the project
columns = [
    "name",
    "owner",
    "language",
    "stargazers_count",
    "forks_count",
    "watchers_count",
    "open_issues_count",
    "created_at",
    "updated_at",
    "license"
]

df = df[columns].copy()

print("\nSelected columns:", len(df.columns))
print("New shape:", df.shape)

# Extract useful values from nested columns
df["owner"] = df["owner"].apply(
    lambda x: eval(x).get("login") if pd.notna(x) else None
)

df["license"] = df["license"].apply(
    lambda x: eval(x).get("name") if pd.notna(x) else None
)

# Handle missing values
df["language"] = df["language"].fillna("Not specified")
df["owner"] = df["owner"].fillna("Unknown")
df["license"] = df["license"].fillna("No license specified")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check for duplicate repositories
print("\nDuplicate repositories:")
print(df.duplicated(subset="name").sum())

# Remove duplicate repositories
df = df.drop_duplicates(subset="name").copy()
print("Shape after removing duplicates:", df.shape)
# Convert date columns
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
df["updated_at"] = pd.to_datetime(df["updated_at"], errors="coerce")

# Rename columns to make them easier to use in SQL
df = df.rename(columns={
    "stargazers_count": "stars",
    "forks_count": "forks",
    "watchers_count": "watchers",
    "open_issues_count": "open_issues",
    "created_at": "created_date",
    "updated_at": "updated_date"
})

# Create simple activity features for later analysis
today = pd.Timestamp.now(tz="UTC")

df["repository_age_years"] = (
    (today - df["created_date"]).dt.days / 365.25
).round(2)

df["days_since_update"] = (
    today - df["updated_date"]
).dt.days

# Save the final dataset
df.to_csv("github_projects.csv", index=False)

print("\nFinal dataset saved as github_projects.csv")
print("Final shape:", df.shape)

# Verify the saved file
check_df = pd.read_csv("github_projects.csv")

print("\nSaved dataset loaded successfully!")
print("Verified shape:", check_df.shape)
print("\nFinal columns:")
print(check_df.columns.tolist())