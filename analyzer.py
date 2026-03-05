import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

raw_data = {
    'Review': [
        "The product is amazing and very fast.",
        "I hated the customer service, it was terrible.",
        "It is an okay tool for the price.",
        "Super quality, I am very happy with my purchase!",
        "The delivery was late and the box was broken."
    ]
}

# Το σώζουμε σε CSV με τον σωστό τρόπο
temp_df = pd.DataFrame(raw_data)
temp_df.to_csv('my_reviews.csv', index=False)
print("Το αρχείο my_reviews.csv δημιουργήθηκε σωστά!")

df = pd.read_csv('my_reviews.csv')
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05: return 'Positive'
    elif score <= -0.05: return 'Negative'
    else: return 'Neutral'

df['Sentiment'] = df['Review'].apply(get_sentiment)

print("\n--- Τελικά Αποτελέσματα ---")
print(df)

# Γράφημα
df['Sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'gray'])
plt.title('Ανάλυση Κριτικών (Final)')
plt.show()