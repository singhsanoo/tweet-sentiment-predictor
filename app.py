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

model_mnb = load(open('nbc.pkl', 'rb'))

model_lgb = load(open('lgb.pkl', 'rb'))

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
    try:
        tweet_vectorized = vectorizer.transform(tweet)

        # Logistic Regression Prediction
        prediction_prob_lrc = (model_lrc.predict_proba(tweet_vectorized)[0] * 100)
        probability_lrc = []

        for element in prediction_prob_lrc:
            prob_0 = str(element)
            prob_0 = prob_0[0:5]
            probability_lrc.append(prob_0)

        # SGD Prediction
        prediction_prob_sgd = (model_sgd.predict_proba(tweet_vectorized)[0] *100)

        probability_clf = []

        for element in prediction_prob_sgd:
            prob_0 = str(element)
            prob_0 = prob_0[0:5]
            probability_clf.append(prob_0)

        # MultinomialNB Prediction
        prediction_prob_mnb = (model_mnb.predict_proba(tweet_vectorized)[0] *100)

        probability_mnb = []

        for element in prediction_prob_mnb:
            prob_0 = str(element)
            prob_0 = prob_0[0:5]
            probability_mnb.append(prob_0)

        # LGB Prediction
        prediction_prob_lgb = (model_lgb.predict_proba(tweet_vectorized)[0] *100)

        probability_lgb = []

        for element in prediction_prob_lgb:
            prob_0 = str(element)
            prob_0 = prob_0[0:5]
            probability_lgb.append(prob_0)
        

        # prediction_text_lrc = f'Logistic Model Prediction : {probability_lrc[0]}% negative / {probability_lrc[1]}% positive'
        # prediction_text_sgd = f'SGD Model Prediction      : {probability_clf[0]}% negative / {probability_clf[1]}% positive'

        return render_template('index.html', pred_txt_lrc_p=probability_lrc[1], \
                                pred_txt_lrc_n=probability_lrc[0], \
                                pred_txt_clf_p=probability_clf[1], \
                                pred_txt_clf_n=probability_clf[0], \
                                pred_txt_mnb_p=probability_mnb[1], \
                                pred_txt_mnb_n=probability_mnb[0], \
                                pred_txt_lgb_p=probability_lgb[1], \
                                pred_txt_lgb_n=probability_lgb[0], \
                                features=request.form['tweet-input'])
    
    except:
        # return render_template('index.html', prediction_text_lrc='Cannot make prediction. Please enter another tweet', prediction_text_sgd='', features=request.form['tweet-input'])
        return render_template('index.html', \
                                cannot_predict='Cannot make prediction. Please enter another tweet', \
                                features=request.form['tweet-input'])

@app.route("/word")
def word():
    return render_template("word_c.html")

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/team")
def team():
    return render_template("team.html")

# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)