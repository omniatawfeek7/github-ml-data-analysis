import sqlite3
import pandas as pd

# Connect to the database
connection = sqlite3.connect("github_repositories.db")

print("Connected to database successfully!")

# Check the total number of repositories
query = """
SELECT COUNT(*) AS total_repositories
FROM repositories;
"""

result = pd.read_sql_query(query, connection)

print("\nTotal repositories:")
print(result)


# Find the most common programming languages
query = """
SELECT language, COUNT(*) AS repository_count
FROM repositories
GROUP BY language
ORDER BY repository_count DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nMost common programming languages:")
print(result)

# Find the most starred repositories
query = """
SELECT name, language, stars, forks
FROM repositories
ORDER BY stars DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\nTop 10 repositories by stars:")
print(result)

# Compare stars and forks
query = """
SELECT name, language, stars, forks
FROM repositories
ORDER BY forks DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\nTop 10 repositories by forks:")
print(result)

# Calculate average stars by programming language
query = """
SELECT
    language,
    COUNT(*) AS repository_count,
    ROUND(AVG(stars), 2) AS average_stars
FROM repositories
GROUP BY language
HAVING COUNT(*) >= 3
ORDER BY average_stars DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nAverage stars by programming language:")
print(result)

# Compare repository age with average stars
query = """
SELECT
    CASE
        WHEN repository_age_years < 5 THEN 'Less than 5 years'
        WHEN repository_age_years < 10 THEN '5 to 10 years'
        ELSE '10 years or more'
    END AS age_group,
    COUNT(*) AS repository_count,
    ROUND(AVG(stars), 2) AS average_stars
FROM repositories
GROUP BY age_group
ORDER BY average_stars DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nAverage stars by repository age:")
print(result)

# Close the database connection
connection.close()