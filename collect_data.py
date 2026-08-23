import requests
import pandas as pd

# GitHub API URL
url = "https://api.github.com/search/repositories"

# Search parameters
params = {
    "q": "machine learning",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

# Send request to GitHub API
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Convert API response to DataFrame
    df = pd.DataFrame(data["items"])

    print("Data collected successfully!")
    print("Number of repositories:", len(df))

    # Save the original dataset
    df.to_csv("github_raw.csv", index=False)

    print("\nRaw dataset saved as github_raw.csv")

    # Basic data quality checks
    print("\nDataset shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nTop columns with missing values:")
    print(df.isnull().sum().sort_values(ascending=False).head(20))

    print("\nDuplicate rows:")
    print(df.duplicated(subset="full_name").sum())   
    print("\nData types:")
    print(df.dtypes)
else:
    print("Failed to retrieve data.")
    print("Status code:", response.status_code)