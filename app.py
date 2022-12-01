# Import libraries
import numpy as np
from flask import Flask, request, render_template
from pickle import load
# import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

# Initialize the flask App
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Helps to avoid cache problems

# Load the model from its pickle file.
model_sgd = load(open('clf.pkl', 'rb'))

model_lrc = load(open('lrc.pkl', 'rb'))

# Load the scaler from its pickle file.
vectorizer = load(open('TfidV.pkl','rb'))

# Remove punctuation
def remove_punct(text):
    new_text = []
    for t in text:
        if t not in string.punctuation:
            new_text.append(t)
    return ''.join(new_text)

# Tokenizer
tokenizer = RegexpTokenizer(r'\w+')

# Removing stop words
def remove_sw(text):
    new_text = []
    for t in text:
        if t not in stopwords.words('english'):
            new_text.append(t)
    return new_text

# Lemmatization
lemmatizer = WordNetLemmatizer()
def word_lemmatizer(text):
    new_text = []
    for t in text:
        lem_text = lemmatizer.lemmatize(t)
        new_text.append(lem_text)
    return new_text

# Define the index route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route that runs when the user clicks the Predict button in the web-app
@app.route('/predict', methods=['POST'])
def predict():
    # Define prediction labels.
    predict_labels = ['Negative', 'Positive']

    tweet = request.form.values()

    #2. Tokenizing etc
    print('tokenizing')
    tweet = remove_punct(tweet)
    tweet = tokenizer.tokenize(tweet.lower())
    tweet = remove_sw(tweet)
    tweet = word_lemmatizer(tweet)

    # 3. Transform each input using the scaler function.
    tweet_vectorized = vectorizer.transform(tweet)

    prediction_prob = np.round(model_lrc.predict_proba(tweet_vectorized)[0], 2) * 100

    prediction_text = f'Negative:  {prediction_prob[0]}% \n Positive:  {prediction_prob[1]}% '

    return render_template('index.html', prediction_text=prediction_text, features=request.form.values())


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)