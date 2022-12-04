# tweet-sentiment-predictor

Gather, tansform, process, clean, split, train, predictions, Calculate , show. 

# Description

We will use datasets to create a model with (various) features that will predict whether a tweet is positive or negative. Using Pandas, AWS, HTML/CSS/JS/Bootstrap, and NLTK they will be ranked and weighted to see which way they get classified.


# Results:

after testing was concluded we had two Model Prediction the SGD Model and a logical model after testing was done it was able to idenetafie the positive and negative tweets after which we then added the information to the 

# Installation/ imports

# Imports
pandas, numpy, NLTK, string, re, dump, RegexpTokenizer, stopwords, TfidfVectorizer, train_test_split, MultinomialNB, confusion_matrix, f1_score, GridSearchCV, SGDClassifier, LogisticRegression, LGBMClassifier. 

## Preprocessing
- Read in the ` to a Pandas DataFrame
- gather data from url store it in pandas use the 'https://uom-twitter-sentiment-analysis.s3.us-east-2.amazonaws.com/Twitter_sentiment_clean.csv' to gather data 
- remove punctuation
- tokenizer
- remove stopwords 
- lematization 
- set data set size 
- 


## Split Cleaned Data into Training Set and Testing Set
- read preprocessed csv
-set x and y values set to 'text' and 'target'
- train, test and split 

## Multinomial Naive Bayes Model
- using MultinomialNB fit X_train, y_train
-set X, Y 
## SGD Model

## Logistic Model

## LGB Model

## Saving the Vectorizer and Models

## Predictions

# Training, and Evaluating the Model:

# project overview  


#Visuals
![1,2,3](https://user-images.githubusercontent.com/93777016/205468893-845257df-4e81-41d3-94b1-d32e9e215afb.png)


# Roadmap

# Authors and acknowledgment
