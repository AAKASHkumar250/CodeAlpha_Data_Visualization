
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("all_books_data.csv")

# Clean and convert data
df["Price"] = df["Price"].astype(str).str.replace("£", "", regex=False).astype(float)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Dashboard style
sns.set_theme(style="whitegrid")

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("BOOKS DATA ANALYSIS DASHBOARD", fontsize=18, fontweight="bold")

# Chart 1: Rating Distribution
sns.countplot(data=df, x="Rating", ax=axes[0, 0])
axes[0, 0].set_title("Books by Rating")
axes[0, 0].set_xlabel("Rating")
axes[0, 0].set_ylabel("Number of Books")

# Chart 2: Price Distribution
sns.histplot(data=df, x="Price", bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Book Price Distribution")
axes[0, 1].set_xlabel("Price (£)")
axes[0, 1].set_ylabel("Number of Books")

# Chart 3: Average Price by Rating
sns.barplot(data=df, x="Rating", y="Price", ax=axes[1, 0])
axes[1, 0].set_title("Average Price by Rating")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Average Price (£)")

# Chart 4: Availability
availability = df["Availability"].value_counts()
axes[1, 1].pie(
    availability,
    labels=availability.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 1].set_title("Book Availability")

plt.tight_layout()
plt.savefig("books_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()

# Display key information
print("\nDASHBOARD SUMMARY")
print("Total Books:", len(df))
print("Average Price: £", round(df["Price"].mean(), 2))
print("Highest Price: £", df["Price"].max())
print("Lowest Price: £", df["Price"].min())
print("Dashboard saved as books_dashboard.png")
