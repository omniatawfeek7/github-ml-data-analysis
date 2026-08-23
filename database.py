import sqlite3
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("github_projects.csv")

print("Cleaned dataset loaded successfully!")
print("Rows:", len(df))

# Create SQLite database
connection = sqlite3.connect("github_repositories.db")

# Store the dataset in a SQLite table
df.to_sql(
    "repositories",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Table 'repositories' created successfully.")

# Check the number of records
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM repositories")

count = cursor.fetchone()[0]

print("Number of records in database:", count)

connection.close()