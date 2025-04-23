import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load CSV
df = pd.read_csv("twitter_training.csv")

# Print column names to confirm structure
print("Columns:", df.columns)

# If you're unsure of the correct column name, inspect a few rows
print(df.head())

# Adjust column name here based on your actual data
# Common names might be: 'Tweet', 'text', 'content', etc.
# Example: If the tweet text is in the 4th column, use df.iloc[:, 3]

tweet_column = df.columns[3]  # Assuming 4th column contains tweet text

# Function to calculate polarity
def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

# Apply polarity calculation
df["Polarity"] = df[tweet_column].apply(get_sentiment)

# Classify sentiment
df["Sentiment"] = df["Polarity"].apply(
    lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
)

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.countplot(x="Sentiment", data=df, palette="Set2")
plt.title("Sentiment Distribution of Tweets")

# Save the plot
plt.savefig("sentiment_distribution.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
