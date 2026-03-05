import streamlit as st
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import ssl
import matplotlib.pyplot as plt

# --- 1. Προετοιμασία AI & SSL ---
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(str(text))['compound']
    if score >= 0.05: return 'Positive'
    elif score <= -0.05: return 'Negative'
    else: return 'Neutral'

# --- 2. Interface με Streamlit ---
st.set_page_config(page_title="AI Sentiment Pro", layout="wide")
st.title(" Advanced AI Sentiment Analyzer")

# Πλευρική μπάρα για επιλογή λειτουργίας
option = st.sidebar.selectbox(
    'Επιλέξτε λειτουργία:',
    ('Live Ανάλυση Κειμένου', 'Ανάλυση Αρχείου CSV')
)

if option == 'Live Ανάλυση Κειμένου':
    st.subheader("Γράψτε το κείμενό σας")
    user_input = st.text_area("Εισάγετε κείμενο στα Αγγλικά:", "This project is amazing!")
    
    if st.button("Ανάλυση"):
        score = sia.polarity_scores(user_input)['compound']
        if score >= 0.05:
            st.success(f"Positive Sentiment (Score: {score})")
            st.balloons()
        elif score <= -0.05:
            st.error(f"Negative Sentiment (Score: {score})")
        else:
            st.warning(f"Neutral Sentiment (Score: {score})")

else:
    st.subheader("Ανεβάστε ένα αρχείο CSV για μαζική ανάλυση")
    uploaded_file = st.file_exists = st.file_uploader("Επιλέξτε το αρχείο .csv", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Προεπισκόπηση Αρχείου:", df.head())
        
        column_name = st.selectbox("Επιλέξτε τη στήλη που περιέχει τα κείμενα:", df.columns)
        
        if st.button("Έναρξη Μαζικής Ανάλυσης"):
            with st.spinner('Το AI αναλύει τα δεδομένα...'):
                df['Sentiment'] = df[column_name].apply(get_sentiment)
            
            st.success("Η ανάλυση ολοκληρώθηκε!")
            
            # Εμφάνιση Στατιστικών και Γραφήματος
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Στατιστικά:")
                st.write(df['Sentiment'].value_counts())
            
            with col2:
                fig, ax = plt.subplots()
                df['Sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#77dd77', '#ff6961', '#fdfd96'], ax=ax)
                ax.set_ylabel('')
                st.pyplot(fig)
            
            # Δυνατότητα Download του νέου αρχείου
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Λήψη Αποτελεσμάτων (CSV)", csv, "analyzed_data.csv", "text/csv")