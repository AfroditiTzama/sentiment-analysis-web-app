# AI Sentiment Analyzer Pro

Μια ολοκληρωμένη web εφαρμογή ανάλυσης συναισθήματος (Sentiment Analysis) που χρησιμοποιεί Τεχνητή Νοημοσύνη για να κατηγοριοποιεί κείμενα ως Θετικά, Αρνητικά ή Ουδέτερα.

##  Δυνατότητες
- **Live Ανάλυση:** Γράψτε το δικό σας κείμενο και δείτε το αποτέλεσμα αμέσως.
- **Μαζική Ανάλυση (Bulk):** Ανεβάστε ένα αρχείο CSV και το AI θα αναλύσει χιλιάδες γραμμές αυτόματα.
- **Οπτικοποίηση:** Αυτόματη δημιουργία γραφημάτων (Pie Charts) για την κατανομή των συναισθημάτων.
- **Export:** Δυνατότητα λήψης των αποτελεσμάτων σε νέο αρχείο CSV.

##  Τεχνολογίες
- **Python 3.x**
- **Streamlit** (Web Interface)
- **NLTK / VADER** (AI Sentiment Model)
- **Pandas** (Data Processing)
- **Matplotlib** (Charts)

##  Εγκατάσταση και Χρήση
Για να τρέξετε την εφαρμογή τοπικά:

1. Κλωνοποιήστε το αποθετήριο:
   ```bash
   git clone https://sentiment-analysis-web-app-c3e8ooefwt3w9m6joltsa2.streamlit.app/

   Εγκαταστήστε τις βιβλιοθήκες:
   pip install -r requirements.txt

   Τρέξτε την εφαρμογή:
   streamlit run app.py
