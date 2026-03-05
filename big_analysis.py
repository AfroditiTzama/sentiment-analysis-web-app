import pandas as pd
import nltk
import ssl
from nltk.corpus import movie_reviews
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# --- 1. Διόρθωση SSL για το Mac ---
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# --- 2. Αυτόματο κατέβασμα των 1.000 κριτικών ---
print(" Ξεκινάω το κατέβασμα των δεδομένων...")
nltk.download('movie_reviews')
nltk.download('vader_lexicon')

# Μετατροπή σε λίστα για την Python
documents = []
for fileid in movie_reviews.fileids()[:1000]: # Παίρνουμε τις πρώτες 1000
    review_text = movie_reviews.raw(fileid)
    documents.append(review_text)

# Δημιουργία Πίνακα
df = pd.DataFrame(documents, columns=['Review'])

# --- 3. Ανάλυση Συναισθήματος ---
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05: return 'Positive'
    elif score <= -0.05: return 'Negative'
    else: return 'Neutral'

print(" Το AI αναλύει τώρα 1.000 κριτικές... Περίμενε λίγο.")
df['Sentiment'] = df['Review'].apply(get_sentiment)

# --- 4. Εμφάνιση Αποτελεσμάτων ---
print("\n--- ΑΠΟΤΕΛΕΣΜΑΤΑ ---")
print(df['Sentiment'].value_counts())

# Δημιουργία Γραφήματος
plt.figure(figsize=(10, 7))
df['Sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c', '#bdc3c7'])
plt.title('Ανάλυση 1.000 Πραγματικών Κριτικών')
plt.show()

# Αποθήκευση των 1.000 κριτικών σε αρχείο Excel/CSV
df.to_csv('1000_reviews_analyzed.csv', index=False)
print("Το αρχείο '1000_reviews_analyzed.csv' δημιουργήθηκε με επιτυχία!")